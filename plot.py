import os
import sys
import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    import uproot3
import json
from coffea import hist
from coffea.util import load
import matplotlib.pyplot as plt
import mplhep as hep
from matplotlib.offsetbox import AnchoredText

sys.path.append("..")
from Hpluscharm_processor.utils.xs_scaler import scale_xs


with open("../Hpluscharm_processor/metadata/mergemap.json") as json_file:
    merge_map = json.load(json_file)

data_err_opts = {
    "linestyle": "none",
    "marker": ".",
    "markersize": 10.0,
    "color": "k",
    "elinewidth": 1,
}
region_map = {
    "SR": "SR $N_j>$1",
    "DY_CRb": "DY+b CR",
    "DY_CRl": "DY+l CR",
    "DY_CRc": "DY+c CR",
    "top_CR": "top CR",
    "DY_CR": "DY CR",
    "SR2": "SR $N_j$==1",
}
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-wf",
        "--workflow",
        default=r"HWW2l2nu",
        help="File identifier to carry through (default: %(default)s)",
    )
    parser.add_argument("-v", "--version", default=r"array", help="version")
    parser.add_argument(
        "--year",
        default=2017,
        type=int,
        required=True,
        help="Scale by appropriate lumi",
    )
    parser.add_argument(
        "--systs", action="store_true", default=False, help="Process systematics"
    )
    parser.add_argument(
        "--flav",
        default="ee",
        choices=["ee", "mumu", "emu", "all"],
        type=str,
        help="flavor",
    )
    parser.add_argument(
        "--region",
        default="SR2",
        choices=["SR", "SR2", "top_CR", "DY_CR", "all"],
        type=str,
        help="Which region in templates",
    )
    # parser.add_argument("-obs_sig", "--observable_sig",type=str,default='ll_mass',help='observable to the fit')
    # parser.add_argument("-obs_bkg", "--observable_bkg",type=str,default='ll_mass',help='observable to the fit')
    parser.add_argument(
        "-obs",
        "--observable",
        type=str,
        default="ll_mass",
        help="observable to the fit",
    )
    parser.add_argument("--prefix", type=str, default="", help="prefix of output")

    args = parser.parse_args()
    print("Running with the following options:")
    print(args)

    outputWWl_s = load(
        f"../Hpluscharm_processor/hists_{args.workflow}_signal_UL17{args.version}.coffea"
    )
    outputWWl_b = load(
        f"../Hpluscharm_processor/hists_{args.workflow}_mcbkg_UL17{args.version}.coffea"
    )
    outputWWl_data = load(
        f"../Hpluscharm_processor/hists_{args.workflow}_data2017{args.version}.coffea"
    )
    outputWWl_dy = load("../Hpluscharm_processor/hists_HWW2l2nu_dym10CR_all.coffea")
    outputWWl_dynlo = load("../Hpluscharm_processor/hists_HWW2l2nu_dy_nlCR_all.coffea")
    outputWWl_dy0j = load("../Hpluscharm_processor/hists_HWW2l2nu_dyarray.coffea")
    eventWWl_s = outputWWl_s["sumw"]
    eventWWl_b = outputWWl_b["sumw"]
    eventWWl_dy = outputWWl_dy["sumw"]
    eventWWl_dynlo = outputWWl_dynlo["sumw"]

    if args.year == 2017:
        lumi = 41500
    if args.year == 2016:
        lumi = 36300
    if args.year == 2018:
        lumi = 59800
    outputWWl_s[args.observable] = scale_xs(
        outputWWl_s[args.observable], lumi, eventWWl_s
    )
    outputWWl_b[args.observable] = scale_xs(
        outputWWl_b[args.observable], lumi, eventWWl_b
    )
    outputWWl_dy[args.observable] = scale_xs(
        outputWWl_dy[args.observable], lumi, eventWWl_dy
    )
    outputWWl_dynlo[args.observable] = scale_xs(
        outputWWl_dynlo[args.observable], lumi, eventWWl_dynlo
    )
    outputWWl_dy0j[args.observable] = scale_xs(
        outputWWl_dy0j[args.observable], lumi, outputWWl_dy0j["sumw"]
    )
    hist_b_nom = outputWWl_b[args.observable].group(
        "dataset", hist.Cat("plotgroup", "plotgroup"), merge_map["hww_tem"]
    )
    hist_b_dy = outputWWl_b[args.observable].group(
        "dataset", hist.Cat("plotgroup", "plotgroup"), merge_map["hww_tem_jetbin"]
    )
    hist_dy0j_jetbin = outputWWl_dy0j[args.observable].group(
        "dataset", hist.Cat("plotgroup", "plotgroup"), merge_map["hww_tem_jetbin"]
    )
    hist_dy_jetbin = outputWWl_dy[args.observable].group(
        "dataset", hist.Cat("plotgroup", "plotgroup"), merge_map["hww_tem_jetbin"]
    )
    hist_dynlo_jetbin = outputWWl_dynlo[args.observable].group(
        "dataset", hist.Cat("plotgroup", "plotgroup"), merge_map["hww_tem_jetbin"]
    )
    hist_dynlo_zptbin = outputWWl_dynlo[args.observable].group(
        "dataset", hist.Cat("plotgroup", "plotgroup"), merge_map["hww_tem_zptbin"]
    )
    hist_dynlo_ptbin = outputWWl_dynlo[args.observable].group(
        "dataset", hist.Cat("plotgroup", "plotgroup"), merge_map["hww_tem_ptbin"]
    )

    outputWWl_data[args.observable] = outputWWl_data[args.observable].group(
        "dataset", hist.Cat("plotgroup", "plotgroup"), merge_map["data"]
    )
    proc_names_bkg = hist_b_nom.axis("plotgroup").identifiers()
    regions = ["SR", "SR2", "top_CR", "DY_CR"]
    flavs = ["ee", "mumu", "emu"]
    for region in ["SR", "SR2", "top_CR", "DY_CR"]:
        if args.region != "all" and args.region != region:
            continue

        for flav in ["ee", "mumu", "emu"]:
            if args.flav != "all" and args.flav != flav:
                continue

            name = "hc"
            name = "data_obs"

            output_bkg_nom = (
                hist_b_nom.integrate("lepflav", flav)
                .integrate("region", region)
                .sum("flav")
            )
            output_bkg_jetbin = (
                hist_b_dy.integrate("lepflav", flav)
                .integrate("region", region)
                .sum("flav")
                .add(
                    hist_dy_jetbin.integrate("lepflav", flav)
                    .integrate("region", region)
                    .sum("flav")
                )
            )
            output_bkg_jetbin = output_bkg_jetbin.add(
                hist_dy0j_jetbin.integrate("lepflav", flav)
                .integrate("region", region)
                .sum("flav")
            )
            # print(hist_dy0j_jetbin.integrate("lepflav",flav).integrate("region",region).sum('flav').values()[()])
            output_bkg_jetbin = output_bkg_jetbin.add(
                hist_dynlo_jetbin.integrate("lepflav", flav)
                .integrate("region", region)
                .sum("flav")
            )
            output_bkg_zptbin = (
                hist_b_dy.integrate("lepflav", flav)
                .integrate("region", region)
                .sum("flav")
                .add(
                    hist_dy_jetbin.integrate("lepflav", flav)
                    .integrate("region", region)
                    .sum("flav")
                )
            )
            output_bkg_zptbin = output_bkg_zptbin.add(
                hist_dy0j_jetbin.integrate("lepflav", flav)
                .integrate("region", region)
                .sum("flav")
            )
            output_bkg_zptbin = output_bkg_zptbin.add(
                hist_dynlo_zptbin.integrate("lepflav", flav)
                .integrate("region", region)
                .sum("flav")
            )
            output_bkg_ptbin = (
                hist_b_dy.integrate("lepflav", flav)
                .integrate("region", region)
                .sum("flav")
                .add(
                    hist_dy_jetbin.integrate("lepflav", flav)
                    .integrate("region", region)
                    .sum("flav")
                )
            )
            output_bkg_ptbin = output_bkg_ptbin.add(
                hist_dy0j_jetbin.integrate("lepflav", flav)
                .integrate("region", region)
                .sum("flav")
            )
            output_bkg_ptbin = output_bkg_ptbin.add(
                hist_dynlo_ptbin.integrate("lepflav", flav)
                .integrate("region", region)
                .sum("flav")
            )

            fig, ((ax), (rax)) = plt.subplots(
                2,
                1,
                figsize=(12, 12),
                gridspec_kw={"height_ratios": (3, 1)},
                sharex=True,
            )
            ax = hist.plot1d(output_bkg_nom.sum("plotgroup"), ax=ax)
            hist.plot1d(output_bkg_jetbin.sum("plotgroup"), ax=ax, clear=False)
            hist.plot1d(output_bkg_zptbin.sum("plotgroup"), ax=ax, clear=False)
            # hist.plot1d(output_bkg_ptbin.sum('plotgroup'),ax=ax,clear=False)
            hist.plot1d(
                outputWWl_data[args.observable]
                .integrate("lepflav", flav)
                .integrate("region", region)
                .sum("flav")
                .integrate("plotgroup", f"data_{flav}"),
                ax=ax,
                clear=False,
                error_opts=data_err_opts,
            )
            leg_label = ax.get_legend_handles_labels()[1]
            leg_label = ["inclusive", "jet bin", "Zpt bin", "data"]
            # leg_label[-1]='Signal'
            # leg_label[-1]='Data'
            ax.legend(loc="upper right", labels=leg_label, fontsize=20)
            at = AnchoredText(
                flav
                + "  "
                + region_map[region]
                + "\n"
                + r"HWW$\rightarrow 2\ell 2\nu$",
                loc="upper left",
                frameon=False,
                prop=dict(size=20),
            )
            ax.add_artist(at)
            ax.set_xlabel(None)
            ax.set_ylim(bottom=0.0001)
            # ax.semilogy()
            hep.mpl_magic(ax=ax)
            rax = hist.plotratio(
                num=outputWWl_data[args.observable]
                .integrate("lepflav", flav)
                .integrate("region", region)
                .sum("flav")
                .integrate("plotgroup", f"data_{flav}"),
                denom=output_bkg_nom.sum("plotgroup"),
                ax=rax,
                error_opts={},
                denom_fill_opts={
                    "alpha": 0.1,
                    "facecolor": (31 / 256, 119 / 256, 180 / 256, 0.5),
                },
                unc="num",
                clear=False,
            )
            hist.plotratio(
                num=outputWWl_data[args.observable]
                .integrate("lepflav", flav)
                .integrate("region", region)
                .sum("flav")
                .integrate("plotgroup", f"data_{flav}"),
                denom=output_bkg_jetbin.sum("plotgroup"),
                ax=rax,
                error_opts={},
                denom_fill_opts={
                    "alpha": 0.1,
                    "facecolor": (255 / 256, 127 / 256, 14 / 256, 0.5),
                },
                unc="num",
                clear=False,
            )
            hist.plotratio(
                num=outputWWl_data[args.observable]
                .integrate("lepflav", flav)
                .integrate("region", region)
                .sum("flav")
                .integrate("plotgroup", f"data_{flav}"),
                denom=output_bkg_zptbin.sum("plotgroup"),
                ax=rax,
                error_opts={},
                denom_fill_opts={
                    "alpha": 0.1,
                    "facecolor": (44 / 256, 160 / 256, 44 / 256, 0.5),
                },
                unc="num",
                clear=False,
            )
            # hist.plotratio(num=outputWWl_data[args.observable].integrate("lepflav",flav).integrate("region",region).sum('flav').integrate('plotgroup',f'data_{flav}'),
            #                                             denom=output_bkg_ptbin.sum('plotgroup'),
            #                                                 ax=rax,
            #                                                 error_opts={},
            #                                                 denom_fill_opts={'alpha': 0.1,'facecolor':(214/256, 39/256, 40/256,0.5)},
            #                                                 unc='num',
            #                                             clear=False
            #                                                 )

            fig.savefig(f"plot/validate_{region}_{flav}_{args.observable}_check.pdf")
