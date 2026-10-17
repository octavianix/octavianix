<img src="assets/banner.svg" width="100%" alt="Suyash Jadhav, with F1 start lights and a car driving off along a track"/>

<img src="assets/ticker.svg" width="100%" alt="Race control: Ph.D. lap 1 underway at the DDOmics Lab, NCCS Pune, since August 2026. Enterotype ET1 under investigation, batch effect confirmed. DRS enabled, new enterotyping pipeline. CRC multi-omics v2.0.0 classified. Survival signal for the 15-gene shortlist noted, no further action."/>

<br/>

<img src="assets/driver.svg" width="100%" alt="Driver card: JAD, Suyash Jadhav, India. DDOmics Lab, NCCS Pune. Bioinformatician and Ph.D. scholar."/>

Hi, I'm Suyash. I'm a bioinformatician and a Ph.D. scholar in the DDOmics Lab at the National Centre for Cell Science, Pune, where I build computational tools to read and make sense of microbiome sequencing data.

I started out with a B.Sc. in Biotechnology in Nashik, then did my M.Sc. at the Bioinformatics Centre, Savitribai Phule Pune University, which is where I moved fully into bioinformatics. I joined NCCS in August 2026 on a CSIR-UGC NET fellowship.

When I'm away from the screen, I'm usually watching Formula 1, which is where the start lights up there come from. 

<img src="assets/pitstop.svg" width="100%" alt="Pit stop, 2024: switched from Biotechnology (B.Sc.) to Bioinformatics (M.Sc. onwards)."/>

<img src="assets/circuit.svg" width="100%" alt="One lap so far: a live-timing style circuit. A car laps the track, braking for corners, while mini-sectors light up, a speed and throttle/brake trace follows it, and a timing tower highlights five milestones: 2021 B.Sc. Biotechnology, Nashik; 2024 GATE-B, AIR 31; 2024 M.Sc. Bioinformatics, SPPU; 2025 CSIR-NET JRF, AIR 105; 2026 Ph.D., DDOmics Lab, NCCS."/>

<br/>

<img src="assets/titles/worked.svg" height="62" alt="Sector 1: Things I've worked on"/>

<img src="assets/card-enterotypes.svg" width="100%" alt="01. Gut enterotypes in India: dissertation, reanalysis in progress. 3,020 people, 17 communities, 5 enterotypes, Prevotella-led."/>

For my dissertation I worked with gut microbiome data from 3,020 people belonging to 17 communities across India, both tribal and non-tribal, along with a food questionnaire that most of them filled in. The question was easy to ask: do Indian guts fall into a few recurring community types, and can you tell which one a person has from what they eat?

*Prevotella* turned out to dominate almost everyone. The model settled on five enterotypes, and which one people carried lined up with their region, how urban their lives were and their diet. I also built a small Shiny app where you answer 34 questions about your diet and it guesses your enterotype. It does better than chance, though honestly not by a lot.

When I went back to the data recently, I found that one of those five groups was mostly samples from low-depth sequencing runs, so it was a batch effect rather than biology. I'm now redoing the analysis with a cleaner pipeline that accounts for sequencing runs, picks the number of enterotypes by a rule fixed in advance, and tests the questionnaire on states it has never seen.

<img src="assets/card-crc.svg" width="100%" alt="02. CRC multi-omics biomarker discovery: v2.0.0, first full run. 557 patients, TCGA, ENCODE and 1000 Genomes, 15-gene shortlist."/>

I wanted to know which genes separate normal colon tissue from early colorectal cancer if you don't rely on differential expression alone. So I took TCGA RNA-seq data from 557 patients and layered chromatin accessibility from ENCODE, survival models, a Bayesian network and South Asian vs European allele frequencies from 1000 Genomes on top. Then I ranked genes by how much of that evidence agreed.

It gave me a shortlist of 15 genes. It also showed that most of what looked like a difference between early and late stage tumours was really a difference in the immune and stromal cells in the samples, and none of the 15 held up for survival once I corrected for multiple testing. Not what I was hoping for, but I'd rather know.

<img src="assets/card-website.svg" width="100%" alt="03. Our lab's website, built for the DDOmics Lab: 24 people, 85 publications, 28 pages, no-code editing."/>

I built the DDOmics Lab website so that nobody would need me to keep it updated. People, publications, news and everything else live in simple table files that anyone in the lab can edit straight on GitHub, and every change gets checked automatically before it goes up.

<br/>

<img src="assets/titles/lately.svg" height="62" alt="Sector 2: lately"/>

Most of what I'm working on right now is still unpublished and lives in private repos, so this graph is the only bit of it you can see for now. It redraws itself every day, the car does a lap underneath it, and my busiest day gets the purple fastest-lap tag.

<img src="assets/contrib.svg" width="100%" alt="Animated contribution graph for the last year, with the busiest day marked as the fastest lap"/>

<img src="assets/next-race.svg" width="100%" alt="Next Formula 1 race, updated daily"/>

<img src="assets/weekend.svg" width="100%" alt="Free practice, what I am learning: comparative genomics of bacterial strains; metabolic modelling of microbial communities; LeetCode, in Python. Season goals: find stable enterotypes in the Indian gut data; validate the diet questionnaire on unseen states; test whether enterosignatures exist in Indian guts."/>

I mostly write R and Python, with a fair amount of Bash holding things together.

<img src="assets/tyres.svg" width="100%" alt="Tyre allocation, the tools I use most: R, Python, Bash, QIIME2, phyloseq, Bioconductor, React, TypeScript."/>

<img src="assets/standings.svg" width="100%" alt="Constructors' standings by size of code in my own repos, October 2026: 1. Python 41.7%, 2. TypeScript 31.8%, 3. R 11.3%, 4. JavaScript 8.5%, 5. Shell 3.1%, 6. CSS 2.1%."/>

<br/>

<img src="assets/titles/hello.svg" height="62" alt="Sector 3: say hello"/>

<img src="assets/radio.svg" width="100%" alt="Team radio from Suyash: If you work on microbiomes, diet and the gut, or your lab has a tool it keeps wishing existed, come on the radio. I'd love to hear about it."/>

Email me at **Suyashjadhav710@gmail.com**, or find me on [LinkedIn](https://www.linkedin.com/in/suyash-jadhav-bioinformatician/), [ORCID](https://orcid.org/0009-0000-1043-7044) and [X](https://x.com/SuyashJ0710).

<img src="assets/footer.svg" width="100%" alt="Chequered flag: thanks for reading"/>
