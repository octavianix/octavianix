<img src="assets/banner.svg" width="100%" alt="Suyash Jadhav, with F1 start lights and a car driving off along a track"/>

<br/>

<img src="assets/img/suyash.png" align="right" width="190" alt="Photo of Suyash"/>

Hi, I'm Suyash. I'm doing my PhD at the National Centre for Cell Science in Pune, in the DDOmics Lab, where I work on microbes and what they do inside us.

I'm a microbiologist first. I got into coding because the sequencing data kept piling up faster than I could deal with it in Excel, and at some point writing a script became quicker than doing things by hand. Now I spend about as much time in a terminal as I do at the bench, and I enjoy both. When I'm doing neither, I'm usually watching Formula 1, which is where the start lights up there come from.

Most of what I build is for the people in my own lab, so I care a lot about whether a tool is easy to install and whether its output can be trusted without me standing next to it.

<br clear="right"/>

<br/>

<img src="assets/titles/worked.svg" height="62" alt="Sector 1: things I've worked on"/>

**Gut enterotypes in India**

For my dissertation I worked with gut microbiome data from 3,020 people belonging to 17 communities across India, both tribal and non-tribal, along with a food questionnaire that most of them filled in. The question was easy to ask: do Indian guts fall into a few recurring community types, and can you tell which one a person has from what they eat?

*Prevotella* turned out to dominate almost everyone. The model settled on five enterotypes, and which one people carried lined up with their region, how urban their lives were and their diet. I also built a small Shiny app where you answer 34 questions about your diet and it guesses your enterotype. It does better than chance, though honestly not by a lot.

When I went back to the data recently, I found that one of those five groups was mostly samples from low-depth sequencing runs, so it was a batch effect rather than biology. I'm now redoing the analysis with a cleaner pipeline that accounts for sequencing runs, picks the number of enterotypes by a rule fixed in advance, and tests the questionnaire on states it has never seen.

**CRC multi-omics biomarker discovery**

I wanted to know which genes separate normal colon tissue from early colorectal cancer if you don't rely on differential expression alone. So I took TCGA RNA-seq data from 557 patients and layered chromatin accessibility from ENCODE, survival models, a Bayesian network and South Asian vs European allele frequencies from 1000 Genomes on top. Then I ranked genes by how much of that evidence agreed.

It gave me a shortlist of 15 genes. It also showed that most of what looked like a difference between early and late stage tumours was really a difference in the immune and stromal cells in the samples, and none of the 15 held up for survival once I corrected for multiple testing. Not what I was hoping for, but I'd rather know.

**Our lab's website**

I built the DDOmics Lab website so that nobody would need me to keep it updated. People, publications, news and everything else live in simple table files that anyone in the lab can edit straight on GitHub, and every change gets checked automatically before it goes up.

<br/>

<img src="assets/titles/lately.svg" height="62" alt="Sector 2: lately"/>

Most of what I'm working on right now is still unpublished and lives in private repos, so this graph is the only bit of it you can see for now. It redraws itself every day, and the car does a lap underneath it.

<img src="assets/contrib.svg" width="100%" alt="Animated contribution graph for the last year"/>

I mostly write R and Python, with a fair amount of Bash holding things together. QIIME2 and phyloseq cover the microbiome side, Bioconductor the rest of the omics, and when something needs a proper interface I use React and TypeScript.

<br/>

<img src="assets/titles/hello.svg" height="62" alt="Sector 3: say hello"/>

If you work on microbiomes, diet and the gut, or your lab has a tool it keeps wishing existed, I'd love to hear about it. You can reach me at **Suyashjadhav710@gmail.com**.

<img src="assets/footer.svg" width="100%" alt="Chequered flag: thanks for reading"/>
