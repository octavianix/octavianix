<img src="assets/banner.svg" width="100%" alt="Suyash Jadhav: microbiologist, bioinformatics, research software. PhD researcher at NCCS Pune, India."/>

<div align="center">

<a href="https://www.nccs.res.in/"><img src="https://img.shields.io/badge/NCCS_Pune-0F766E?style=flat-square&logo=bookstack&logoColor=white" alt="NCCS Pune"/></a>
<a href="mailto:Suyashjadhav710@gmail.com"><img src="https://img.shields.io/badge/Email-0B3D3A?style=flat-square&logo=gmail&logoColor=white" alt="Email"/></a>
<img src="https://komarev.com/ghpvc/?username=octavianix&style=flat-square&color=0f766e&label=views" alt="Profile views"/>

<sub>

**[About](#about)** &nbsp;·&nbsp; **[Research](#research)** &nbsp;·&nbsp; **[Finished work](#projects)** &nbsp;·&nbsp; **[Toolbox](#toolbox)** &nbsp;·&nbsp; **[Activity](#activity)** &nbsp;·&nbsp; **[Contact](#connect)**

</sub>

</div>

<a id="about"></a>
<img src="assets/titles/about.svg" width="100%" alt="About"/>

I'm a **microbiologist who learned to code because the questions got bigger than the spreadsheet.** I'm doing my PhD at the **DDOmics Lab, National Centre for Cell Science (NCCS), Pune**. I study how microbial communities shape human health, and I build the software that makes that work repeatable.

- 🔭 &nbsp;**Working on:** gut microbiome and microbial genomics, kept in the lab notebook until it's finished
- 🧪 &nbsp;**Shipped:** [SangerCap](#projects), from Sanger traces to a defensible microbial ID in one command
- 🌱 &nbsp;**Learning:** metabolic modelling, better ML validation, and one LeetCode problem at a time
- 🤝 &nbsp;**Open to:** microbiome collaborations and research software for labs
- ⚡ &nbsp;**Fun fact:** I culture the bugs *and* write the pipelines, so I wear gloves and a terminal

<a id="research"></a>
<img src="assets/titles/research.svg" width="100%" alt="Research areas"/>

<table>
<tr>
<td align="center" width="25%"><h3>🦠</h3><b>Gut microbiome</b><br/><sub>Community structure, diet and host factors</sub></td>
<td align="center" width="25%"><h3>🧬</h3><b>Microbial genomics</b><br/><sub>Isolates, identification and comparative genomics</sub></td>
<td align="center" width="25%"><h3>🎗️</h3><b>Cancer multi-omics</b><br/><sub>Transcriptomics, chromatin and survival in CRC</sub></td>
<td align="center" width="25%"><h3>🛠️</h3><b>Research software</b><br/><sub>Reproducible pipelines and tools for wet labs</sub></td>
</tr>
</table>

<a id="projects"></a>
<img src="assets/titles/projects.svg" width="100%" alt="Finished work"/>

> [!NOTE]
> Source code for these projects is private for now. Ask me for access or a walkthrough.

<table>
<tr>
<td width="46%" valign="middle"><img src="assets/sangercap-trace.svg" width="100%" alt="A real Sanger chromatogram from SangerCap's test data"/></td>
<td width="54%" valign="top">

### 🧪 SangerCap
<img src="https://img.shields.io/badge/v2.0.2-released-14B8A6?style=flat-square" alt="v2.0.2 released"/> <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/> <img src="https://img.shields.io/badge/GPL--3.0-555?style=flat-square" alt="GPL-3.0"/>

Identifies microbial isolates from `.ab1` Sanger traces in one command. It trims with TraceTuner, assembles with CAP3, identifies with BLAST plus global alignment, then calls a taxonomic rank. Every sample gets a review flag for mixed cultures, species ties or partial matches. It runs as a Windows/macOS desktop app or a CLI, and every run writes a manifest with tool versions and checksums.

<sub>**Why v2 exists:** v1 was a FastAPI + Celery + Redis + Docker web app that took eight steps to install. I rebuilt it as one installable program, because the best architecture is the one labmates can actually install.</sub>

</td>
</tr>
<tr>
<td width="46%" valign="middle"><img src="assets/img/crc-volcano.png" width="100%" alt="Volcano plot: 1,646 up- and 1,593 down-regulated genes, normal colon vs stage I/II tumours"/></td>
<td width="54%" valign="top">

### 🎗️ CRC Multi-Omics Biomarker Discovery
<img src="https://img.shields.io/badge/v2.0.0-released-14B8A6?style=flat-square" alt="v2.0.0 released"/> <img src="https://img.shields.io/badge/R-276DC3?style=flat-square&logo=r&logoColor=white" alt="R"/> <img src="https://img.shields.io/badge/Bioconductor-1A81C2?style=flat-square" alt="Bioconductor"/>

Ranks colorectal cancer biomarkers by how much evidence converges on them. It combines TCGA RNA-seq, ENCODE promoter accessibility, adjusted survival models, a bootstrapped Bayesian network, patient-level LASSO and 1000 Genomes South Asian vs European allele frequencies.

**First full run:** 557 patients · 3,239 genes changed between normal colon and stage I/II tumours · a 15-gene candidate panel · stage classifier AUC 0.70.

<sub>**Reported honestly:** the stage signal mostly reflected immune and stromal composition, and no candidate survived multiple-testing correction for survival.</sub>

</td>
</tr>
<tr>
<td width="46%" valign="middle"><img src="assets/img/ddomics-website.jpg" width="100%" alt="Home page of the DDOmics Lab website"/></td>
<td width="54%" valign="top">

### 🌐 DDOmics Lab Website
<img src="https://img.shields.io/badge/built-14B8A6?style=flat-square" alt="built"/> <img src="https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB" alt="React"/> <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript"/>

The site for Dr. Dhiraj Dhotre's lab at NCCS covers 24 people, 85 publications, research, facilities and news. All content lives in plain `.tsv` and `.md` files that labmates edit on GitHub without code. Every change is validated, type-checked and built in CI, and all 28 pages are prerendered for GitHub Pages.

</td>
</tr>
</table>

<a id="toolbox"></a>
<img src="assets/titles/toolbox.svg" width="100%" alt="Toolbox"/>

| Area | Tools |
|:--|:--|
| **Languages** | <img src="https://skillicons.dev/icons?i=r,python,bash,ts&theme=dark" height="36" alt="R, Python, Bash, TypeScript"/> |
| **Omics & stats** | ![Bioconductor](https://img.shields.io/badge/Bioconductor-1A81C2?style=flat-square) ![DESeq2](https://img.shields.io/badge/DESeq2-0F766E?style=flat-square) ![clusterProfiler](https://img.shields.io/badge/clusterProfiler-14B8A6?style=flat-square) ![survival](https://img.shields.io/badge/survival_·_glmnet_·_bnlearn-276DC3?style=flat-square) ![BLAST+](https://img.shields.io/badge/BLAST+_·_CAP3_·_MAFFT-005A9C?style=flat-square) |
| **ML & data** | ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white) ![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white) |
| **Workflows & infra** | ![Nextflow](https://img.shields.io/badge/Nextflow_·_nf--core-24B064?style=flat-square&logo=nextflow&logoColor=white) ![Conda](https://img.shields.io/badge/Conda-44A833?style=flat-square&logo=anaconda&logoColor=white) ![Linux](https://img.shields.io/badge/Linux_·_SSH-333333?style=flat-square&logo=linux&logoColor=white) ![Git](https://img.shields.io/badge/Git_·_Actions-F05032?style=flat-square&logo=git&logoColor=white) |
| **Web** | <img src="https://skillicons.dev/icons?i=react,vite,tailwind,nodejs&theme=dark" height="36" alt="React, Vite, Tailwind, Node.js"/> |
| **Wet lab** | Culturing and isolation · DNA extraction · Sanger and 16S sequencing · Microbial identification |

<a id="activity"></a>
<img src="assets/titles/activity.svg" width="100%" alt="Activity"/>

<!-- Redrawn daily from your contribution calendar by .github/workflows/contrib-graph.yml -->
<img src="assets/contrib.svg" width="100%" alt="Animated contribution graph for the last year"/>

```diff
+ 2026-03-15   SangerCap 1.0.0         web app: FastAPI · Celery · Redis · React · Docker
+ 2026-08      DDOmics Lab website     content editable without code, validated in CI
+ 2026-10-02   SangerCap 2.0.0         rebuilt as a desktop app and CLI
+ 2026-10-05   SangerCap 2.0.2         scheduled runs on the lab server
+ 2026-10-15   CRC Multi-Omics 2.0.0   first complete run and results report
```

#### How I work

| 📜 Scope first | 🔁 Reproducible | 📖 Documented | 🧑‍🔬 Usable |
|:--|:--|:--|:--|
| Each project says what it can and cannot claim. | Config files, not magic numbers. Run manifests with checksums. | Why each method was chosen and how to run it. | Installers, review flags, no-code editing. |

<a id="connect"></a>
<img src="assets/titles/connect.svg" width="100%" alt="Let's connect"/>

<div align="center">

I'm happy to talk about microbiomes, Sanger data, or a tool your lab keeps wishing it had.

<a href="mailto:Suyashjadhav710@gmail.com"><img src="https://img.shields.io/badge/Email_me-0F766E?style=for-the-badge&logo=gmail&logoColor=white" alt="Email me"/></a>

<img src="assets/footer.svg" width="100%" alt="Thanks for reading"/>

</div>
