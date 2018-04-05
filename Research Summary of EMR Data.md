# Research Summary of Electronic Medical Records Data
# 电子病历数据的研究摘要
---

## Introduction
主要介绍国内外在电子病历应用领域的研究内容和研究方向
精准医疗的一个主要目标就是开发出针对患者的量化模型，可以预测健康状况，帮助预防疾病，甚至辅助诊断、临床决策和治疗。临床电子病历（electronic health records, EHRs）显示了在这个领域很多可能性。[1]
电子病历的二次运用可以进行：

* 数据驱动的药物疗效和相互作用的预测[2]
* 发现二型糖尿病的子类[3]
* 发现自闭症谱系障碍合并症集群[4]
* 改善临床试验招募患者[5]

但在临床决策支持系统中没有广泛应用。

临床电子病例由于其高维度、有噪音、异质性、稀疏性、不完整性、随机错误以及系统偏性，使得临床病例的机器学习应用十分困难。[6,7]

预测算法很大程度基于特征选取和数据表示。传统的电子病历应用时找一个该领域专家制定所需寻找的特征（如学习目标和寻找目标），然后用临时方式来指定临床变量。

为了克服这些缺陷，数据驱动的电子病历特征选择方法被开发出来。这些方法的一个限制时患者通常用一个二维向量来表示，由临床数据仓库中所有数据描述组成。这种表示方式稀疏、有噪音、重复性，不适宜对电子病历中隐藏或嵌入的分层信息建模。

## 电子病历在药物治疗领域的应用
### 不良药物事件（Adverse Drug Events）
不良药物事件仍然是世界各地药物治疗中发病和死亡的一个主要原因。很多药物不良反应在药物上市前临床试验中没有被发现。[8]

许多不良反应是很罕见的，只在很少的人群中发生。

不过，作为上市后监管的一个重要环节，大量药物上市后的不良事件报告机制（adverse event reporting systems, AERSs）提供了一个研究大量患者人群药物效应的机会。但是，共同使用的药物、患者人口统计学、患者病史等信息在不良事件报告系统中很难体现，这些也限制了量化特征提取分析。

两个数据库：
* 药物综合效应数据库（comprehensive database of drug effects , OFFSIDES）[9]  http://tatonettilab.org/resources/tatonetti-stm.html
* 药物相互作用引发副作用数据库（database of drug-drug interaction side effects, TWOSIDES）[9]

基于临床副作用的药物相互作用标签传播预测：
Supplements
Label Propagation Prediction of Drug-Drug Interactions Based on Clinical Side-Effects
https://astro.temple.edu/~tua87106/ddi.html
（包含多个药物相互作用和副作用数据库，可供查阅下载）

### 药物引发的肝损伤（Drug-induced liver injury, DILI）

药物引发的肝损伤一直过去50年是最频繁的药物安全相关的问题[12]。开了了一种基于深度学习架构的药物引发肝损伤模型，对475个药物的训练集训练模型，使用198个药物的验证集进行验证，准确率（accuracy）86.9%,敏感性（sensitivity）82.5%，特异性（specificity）92.9%，AUC值0.955[10]

超过700种药物发现与肝损伤相关[11]



## 参考文献
[1] Hersh, W. R. Adding value to the electronic health record through secondary use of data for quality assurance, research, and
surveillance. Am. J. Manag. Care 13, 277–278 (2007)
[2] Tatonetti, N. P., Ye, P. P., Daneshjou, R. & Altman, R. B. Data-driven prediction of drug effects and interactions. Sci. Transl. Med. 4,
125ra131 (2012).
[3] Li, L. et al. Identification of type 2 diabetes subgroups through topological analysis of patient similarity. Sci. Transl. Med. 7, 311ra174
(2015).
[4] Doshi-Velez, F., Ge, Y. & Kohane, I. Comorbidity clusters in autism spectrum disorders: an electronic health record time-series
analysis. Pediatrics 133, e54–63 (2014).
[5] Miotto, R. & Weng, C. Case-based reasoning using electronic health records efficiently identifies eligible patients for clinical trials. J. Am. Med. Inform. Assoc. 22, E141–E150 (2015).
[6] Jensen, P. B., Jensen, L. J. & Brunak, S. Mining electronic health records: towards better research applications and clinical care. Nat. Rev. Genet. 13, 395–405 (2012).
[7] Weiskopf, N. G., Hripcsak, G., Swaminathan, S. & Weng, C. Defining and measuring completeness of electronic health records for secondary use. J. Biomed. Inform. 46, 830–836 (2013).
[8] Classen DC, Pestotnik SL, Evans RS, Lloyd JF, Burke JP. Adverse drug events in hospitalized patients. Excess length of stay, extra costs, and attributable mortality. JAMA.1997; 277:301–306. [PubMed: 9002492]
[9] (Tatonetti et al., 2012) Data-driven prediction of drug effects and interactions. Sci Transl Med. PMID: 22422992 DOI: 10.1126/scitranslmed.3003377
[10] Xu Y, Dai Z, Chen F, et al. Deep Learning for Drug-Induced Liver Injury[J]. Journal of Chemical Information and Modeling, 2015, 55(10): 2085-2093.
[11] Hoofnagle, J. H.; Serrano, J.; Knoben, J. E.; Navarro, V. J. Livertox: A Website on Drug-Induced Liver Injury. Hepatology 2013, 57, 873−874
[12] Assis, D. N.; Navarro, V. J. Human Drug Hepatotoxicity: A Contemporary Clinical Perspective. Expert Opin. Drug Metab. Toxicol. 2009, 5, 463−473.