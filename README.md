# NLPCC2024 Shared Task 3: Dialogue-level Coreference Resolution and Relation Extraction

## Introduction

### Background

Dialogue Relation Extraction (DRE) focuses on the relations between arguments in a conversation, which can help better understand the interaction between interlocutors. The phenomenon of reference is widely present in natural language, especially in conversations. Dialogue coreference resolution can provide more accurate contextual understanding for DRE task. We introduce dialogue level coreference resolution and relation extraction task, and evaluate the model's ability to recognize dialogue level coreference information and extract relations using coreference information.

### Task Requirements

Coreference resolution: identifying different expressions pointing to the same entity in a conversation;

Dialogue relation extraction: Using the results of coreference resolution to help identify the relationships between argument pairs in a conversation.

## Updates

All updates about this shared task will be posted on this page.

## Important Dates

- 2023/03/25：registration open
- 2023/04/15：release of detailed task guidelines & training data
- 2023/05/25：registration deadline
- 2023/06/11：release of test data
- 2023/06/20：participants’ results submission deadline
- 2023/06/30：evaluation results release and call for system reports and conference paper


## Team Rank
| rank | team member | team | task1-F1 | task2-F1 | average-F1 |
| ---- | ---- | ------------- | ------------- | -------------- | -------------- |

## Dataset

The dataset for this evaluation is based on our dataset published in NLPCC2023, DialogREC+: An Extension of DialogRE to Investigate How Much Core Reference Helps Relationship Extraction in Dialogs.
The data provided is as follows:

| train set | dev set | test set | total |
| ---- | ---- | ----|----|
| 1073 | 358 | 357 | 1788 |

The data is explained as follows:

A piece of data corresponds to a dictionary. 
`dialog` is a dialogue list, `relations` is the triplet information of the relationship, 
where `x` and `y` are subject and object respectively, 
`r` is the relation type,
`rid` is the corresponding id of `r`, 
`t` is the trigger, 
`x_type` and `y_type` are the types of subject and object respectively,
`mentions` and `clusters` respectively refer to the coreferential words and their positions in the dialogue.

In the test set, the fields `rid`, `r`, `t`, `mentions`, and `clusters` are empty.


## Evaluation


### Subtask 1：Coreference resolution
Input the dialogue, 
contestants need to predict multiple coreference chains in the dialogue.
We use the official CoNLL-2012 evaluation script to calculate the F1 score of `MUC`, `B3`, and `CEAF`.

### Subtask 2：Dialogue relation extraction
Participants need to predict the relations between argument pairs based on the dialogue, 
and **must** use the coreference information of subtask 1 to help understand the dialogue. Mainly focus on three indicators: Precision (P), Recall (R), and F1 value (F1).

### Evaluation Method
* The final score of Subtask 1 is the average F1;
* Take the F1 score as the final score for Subtask 2;
* The average score of two subtasks will be used as the overall score of the entire task;
* We will provide evaluation scripts in the coming days.

## Testing Instructions and Submission

The test data format is consistent with the training and validation sets, and participants need to predict the empty `clusters` and `rid` fields.

For submission, the following materials should be packaged as one `zip` file and sent to yiyunxiong@whu.edu.cn.

* Submission File: Please write the final result into the `clusters` and `rid` fields of the test set, consistent with the training set format.
* Code: The code folder should contain all the codes of data augmentation, data processing, model training and model inference.
* Document:
  * Sharing Link of Additional Data: Additional data used in the experiment should be uploaded to a cloud storage, i.e., net disk, and the sharing link should be included in the document.
  * Code Reproduction Process: The submitted code may be checked and reproduced by us, so please briefly explain the process of reproducing the code in the document.

  
If you have any questions, please contact [yiyunxiong@whu.edu.cn](mailto:yiyunxiong@whu.edu.cn) via email.
