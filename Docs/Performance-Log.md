# Performance Logs

## Model with Responses Token Size – _176_

### Training Results

| Epoch | Training Loss | Validation Loss |
| ----- | ------------- | --------------- |
| _1_   | _2.610100_    | _1.296181_      |
| _2_   | _0.783800_    | _0.847100_      |
| _3_   | _0.682800_    | _0.762251_      |
| _4_   | _0.645500_    | _0.717920_      |
| _5_   | _0.624500_    | _0.708243_      |

## Model with Responses Token Size – _200_

### Training Results

| Epoch | Training Loss | Validation Loss |
| ----- | ------------- | --------------- |
| _1_   | _2.712300_    | _1.069297_      |
| _2_   | _0.758300_    | _0.804383_      |
| _3_   | _0.691500_    | _0.764833_      |
| _4_   | _0.652400_    | _0.734626_      |
| _5_   | _0.637500_    | _0.715247_      |

## Model with Responses Token Size – _303_

### Training Results

| Epoch | Training Loss | Validation Loss |
| ----- | ------------- | --------------- |
| _0_   | _2.833000_    | _1.127712_      |
| _1_   | _0.766000_    | _0.833765_      |
| _2_   | _0.681300_    | _0.756103_      |
| _4_   | _0.633200_    | _0.721219_      |

## 1st Model with Token Size – 440

- `learning_rate: 2e-5`
- `per_device_train_batch_size: 8`
- `per_device_eval_batch_size: 8`
- `num_train_epochs: 5`
- `gradient_accumulation_steps: 8`
- `evaluation_strategy: "epoch"`
- `save_strategy: "epoch"`
- `save_total_limit: 3`
- `fp16: True`
- `weight_decay: 0.01`
- `logging_steps: 200`
- `load_best_model_at_end: True`
- `warmup_steps: 500`
- `report_to: "none"`
- `gradient_checkpointing: True`

## Training Results

| Epoch | Training Loss | Validation Loss |
| ----- | ------------- | --------------- |
| _0_   | _4.805200_    | _1.225489_      |
| _1_   | _0.786700_    | _0.801719_      |
| _2_   | _0.690400_    | _0.755417_      |
| _4_   | _0.642500_    | _0.724628_      |

## Evaluation

### 0.01% Validation Set

- **BLEU-1 Score**: _53.40_
- **BLEU-2 Score**: _21.57_
- **BLEU-3 Score**: _10.89_
- **BLEU-4 Score**: _8.00_
- **Total Time**: _11.05s_
- **Average Time per Response**: _1.38s_

### 0.1% Validation Set

- **BLEU-1 Score**: _83.50_
- **BLEU-2 Score**: _46.08_
- **BLEU-3 Score**: _20.79_
- **BLEU-4 Score**: _14.00_
- **Total Time**: _107.76s_
- **Average Time per Response**: _1.35s_

### 1% Validation Set

- **BLEU-1 Score**: _93.20_
- **BLEU-2 Score**: _82.35_
- **BLEU-3 Score**: _52.48_
- **BLEU-4 Score**: _31.00_
- **Total Time**: _1004.45s_
- **Average Time per Response**: _1.25s_

### 10% Validation Set

- **BLEU-1 Score**: _100.0_
- **BLEU-2 Score**: _94.11_
- **BLEU-3 Score**: _80.20_
- **BLEU-4 Score**: _59.0_
- **Total Time**: _10253s_
- **Average Time per Response**: _1.27s_

## 2nd Model with Token Size – 440

- `learning_rate: 3e-5`
- `per_device_train_batch_size: 12`
- `per_device_eval_batch_size: 12`
- `num_train_epochs: 7`
- `gradient_accumulation_steps: 5`
- `evaluation_strategy: "epoch"`
- `save_strategy: "epoch"`
- `save_total_limit: 3`
- `fp16: True`
- `weight_decay: 0.01`
- `logging_steps: 200`
- `load_best_model_at_end: True`
- `warmup_steps: 500`
- `report_to: "none"`
- `gradient_checkpointing: True`
- `lr_scheduler_type: "cosine"`
- `eval_accumulation_steps: 10`

## Training Results

| Epoch | Training Loss | Validation Loss |
| ----- | ------------- | --------------- |
| _1_   | _1.280400_    | _1.306809_      |
| _2_   | _0.738200_    | _0.787249_      |
| _3_   | _0.654700_    | _0.748505_      |
| _4_   | _0.590900_    | _0.693028_      |
| _5_   | _0.563000_    | _0.676866_      |
| _6_   | _0.539300_    | _0.670430_      |
| _7_   | _0.529600_    | _0.670399_      |

# Evaluation

## 0.01% Validation Set:

### BLEU Scores:

- **BLEU-1 Score**: _54.24_
- **BLEU-2 Score**: _23.08_
- **BLEU-3 Score**: _12.07_
- **BLEU-4 Score**: _7.83_

### ROUGE Scores:

- **ROUGE-1 Score**: _0.53_
- **ROUGE-2 Score**: _0.27_
- **ROUGE-L Score**: _0.36_

### METEOR Score:

- **METEOR Score**: _0.42_

### Latency Metrics:

- **Total time for generating responses**: _11.55s_
- **Average time per response**: _1.44s_
- **95th Percentile Response Time**: _3.10s_

### TER Score:

- **TER Score**: _0.78_

### ChrF Scores:

- **ChrF3 Score**: _56.29_

### COMET Score:

- **Average COMET Score (from individual scores)**: _0.13_
- **System-level COMET Score**: _0.13_

## 0.1% Validation Set:

### BLEU Scores:

- **BLEU-1 Score**: _84.75_
- **BLEU-2 Score**: _47.86_
- **BLEU-3 Score**: _25.00_
- **BLEU-4 Score**: _16.52_

### ROUGE Scores:

- **ROUGE-1 Score**: _0.55_
- **ROUGE-2 Score**: _0.30_
- **ROUGE-L Score**: _0.38_

### METEOR Score:

- **METEOR Score**: _0.46_

### Latency Metrics:

- **Total time for generating _80_ responses**: _96.37s_
- **Average time per response**: _1.20s_
- **95th Percentile Response Time**: _2.20s_

### TER Score:

- **TER Score**: _0.90_

### ChrF Scores:

- **ChrF3 Score**: _56.29_

### COMET Score:

- **Average COMET Score (from individual scores)**: _0.17_
- **System-level COMET Score**: _0.17_

## 1% Validation Set:

### BLEU Scores:

- **BLEU-1 Score**: _98.31_
- **BLEU-2 Score**: _85.47_
- **BLEU-3 Score**: _59.48_
- **BLEU-4 Score**: _38.26_

### ROUGE Scores:

- **ROUGE-1 Score**: _0.55_
- **ROUGE-2 Score**: _0.30_
- **ROUGE-L Score**: _0.38_

### METEOR Score:

- **METEOR Score**: _0.45_

### Latency Metrics:

- **Total time for generating _806_ responses**: _1000.01s_
- **Average time per response**: _1.24s_
- **95th Percentile Response Time**: _2.31s_

### TER Score:

- **TER Score**: _0.83_

### ChrF Scores:

- **ChrF3 Score**: _56.29_

### COMET Score:

- **Average COMET Score (from individual scores)**: _0.19_
- **System-level COMET Score**: _0.19_

## 10% Validation Set:

### BLEU Scores:

- **BLEU-1 Score**: _100.00_
- **BLEU-2 Score**: _93.16_
- **BLEU-3 Score**: _81.03_
- **BLEU-4 Score**: _61.74_

### ROUGE Scores:

- **ROUGE-1 Score**: _0.55_
- **ROUGE-2 Score**: _0.30_
- **ROUGE-L Score**: _0.38_

### METEOR Score:

- **METEOR Score**: _0.45_

### Latency Metrics:

- **Total time for generating _8061_ responses**: _10100.69s (≈ 2.8hrs)_
- **Average time per response**: _1.25s_
- **95th Percentile Response Time**: _2.34s_

### TER Score:

- **TER Score**: _0.73_

### ChrF Scores:

- **ChrF3 Score**: _64.33_
- **ChrF Score**: _61.39_
- **ChrF++ Score**: _58.56_

### COMET Score:

- **Average COMET Score (from individual scores)**: _0.18_
- **System-level COMET Score**: _0.18_

## 20% Validation Set:

### BLEU Scores:

- **BLEU-1 Score**: _100.00_
- **BLEU-2 Score**: _96.58_
- **BLEU-3 Score**: _86.21_
- **BLEU-4 Score**: _72.17_

### ROUGE Scores:

- **ROUGE-1 Score**: _0.55_
- **ROUGE-2 Score**: _0.30_
- **ROUGE-L Score**: _0.38_

### METEOR Score:

- **METEOR Score**: _0.45_

### Latency Metrics:

- **Total time for generating _16123_ responses**: _19702.30s (≈ 5.4hrs)_
- **Average time per response**: _1.22s_
- **95th Percentile Response Time**: _2.28s_

### TER Score:

- **TER Score**: _0.65_

### ChrF Scores:

- **ChrF3 Score**: _68.86_
- **ChrF Score**: _66.44_
- **ChrF++ Score**: _64.09_

### COMET Score:

- **Average COMET Score (from individual scores)**: _0.18_
- **System-level COMET Score**: _0.18_

### 10% Test Data from each Language:

#### BLEU Score Evaluation for All Languages:

- **BLEU Scores for English**:

  - BLEU-1 Score: _100.00_
  - BLEU-2 Score: _99.02_
  - BLEU-3 Score: _95.05_
  - BLEU-4 Score: _88.00_

- **BLEU Scores for French**:

  - BLEU-1 Score: _100.00_
  - BLEU-2 Score: _99.11_
  - BLEU-3 Score: _96.40_
  - BLEU-4 Score: _93.64_

- **BLEU Scores for Spanish**:
  - BLEU-1 Score: _100.00_
  - BLEU-2 Score: _100.00_
  - BLEU-3 Score: _95.15_
  - BLEU-4 Score: _86.27_

#### ROUGE Score Evaluation for All Languages:

- **ROUGE Scores for English**:

  - ROUGE-1 Score: _0.58_
  - ROUGE-2 Score: _0.31_
  - ROUGE-L Score: _0.41_

- **ROUGE Scores for French**:

  - ROUGE-1 Score: _0.53_
  - ROUGE-2 Score: _0.29_
  - ROUGE-L Score: _0.36_

- **ROUGE Scores for Spanish**:
  - ROUGE-1 Score: _0.53_
  - ROUGE-2 Score: _0.29_
  - ROUGE-L Score: _0.37_

#### METEOR Score Evaluation for All Languages:

- **METEOR Score for English**: _0.48_
- **METEOR Score for French**: _0.43_
- **METEOR Score for Spanish**: _0.43_

#### TER Score Evaluation for All Languages:

- **TER Score for English**: _0.60_
- **TER Score for French**: _0.55_
- **TER Score for Spanish**: _0.58_

#### ChrF Scores Evaluation for All Languages:

- **ChrF Score for English**: _59.77_
- **ChrF3 Score for English**: _62.93_

- **ChrF Score for French**: _62.62_
- **ChrF3 Score for French**: _64.41_

- **ChrF Score for Spanish**: _64.45_
- **ChrF3 Score for Spanish**: _70.05_

#### Latency Evaluation for All Languages:

- **English**:

  - **Average Response Time**: _1.19s_
  - **95th Percentile Response Time**: _2.05s_

- **French**:

  - **Average Response Time**: _1.30s_
  - **95th Percentile Response Time**: _2.52s_

- **Spanish**:
  - **Average Response Time**: _1.21s_
  - **95th Percentile Response Time**: _2.21s_

#### COMET Score Evaluation for All Languages:

- **English**:

  - **Average COMET Score (from individual scores)**: _0.16_
  - **System-level COMET Score**: _0.16_

- **French**:

  - **Average COMET Score (from individual scores)**: _0.14_
  - **System-level COMET Score**: _0.14_

- **Spanish**:
  - **Average COMET Score (from individual scores)**: _0.26_
  - **System-level COMET Score**: _0.26_

---

### 20% Test Data from each Language:

#### BLEU Score Evaluation for All Languages:

- **BLEU Scores for English**:

  - BLEU-1 Score: _100.00_
  - BLEU-2 Score: _100.00_
  - BLEU-3 Score: _98.02_
  - BLEU-4 Score: _92.00_

- **BLEU Scores for French**:

  - BLEU-1 Score: _100.00_
  - BLEU-2 Score: _100.00_
  - BLEU-3 Score: _98.20_
  - BLEU-4 Score: _95.45_

- **BLEU Scores for Spanish**:
  - BLEU-1 Score: _100.00_
  - BLEU-2 Score: _100.00_
  - BLEU-3 Score: _98.06_
  - BLEU-4 Score: _93.14_

#### ROUGE Score Evaluation for All Languages:

- **ROUGE Scores for English**:

  - ROUGE-1 Score: _0.58_
  - ROUGE-2 Score: _0.32_
  - ROUGE-L Score: _0.41_

- **ROUGE Scores for French**:

  - ROUGE-1 Score: _0.53_
  - ROUGE-2 Score: _0.29_
  - ROUGE-L Score: _0.36_

- **ROUGE Scores for Spanish**:
  - ROUGE-1 Score: _0.53_
  - ROUGE-2 Score: _0.29_
  - ROUGE-L Score: _0.37_

#### METEOR Score Evaluation for All Languages:

- **METEOR Score for English**: _0.48_
- **METEOR Score for French**: _0.43_
- **METEOR Score for Spanish**: _0.43_

#### TER Score Evaluation for All Languages:

- **TER Score for English**: _0.54_
- **TER Score for French**: _0.55_
- **TER Score for Spanish**: _0.58_

#### ChrF, ChrF3, and ChrF++ Score Evaluation for All Languages:

- **ChrF Scores for English**:

  - **ChrF**: _62.69_
  - **ChrF3**: _64.37_
  - **ChrF++**: _61.07_

- **ChrF Scores for French**:

  - **ChrF**: _67.06_
  - **ChrF3**: _71.44_
  - **ChrF++**: _66.45_

- **ChrF Scores for Spanish**:
  - **ChrF**: _64.45_
  - **ChrF3**: _70.05_
  - **ChrF++**: _61.41_

#### Latency Evaluation for All Languages:

- **English**:

  - **Average Response Time**: _1.18s_
  - **95th Percentile Response Time**: _2.04s_

- **French**:

  - **Average Response Time**: _1.28s_
  - **95th Percentile Response Time**: _2.46s_

- **Spanish**:
  - **Average Response Time**: _1.21s_
  - **95th Percentile Response Time**: _2.20s_

#### COMET Score Evaluation for All Languages:

- **English**:

  - **Average COMET Score (from individual scores)**: _0.16_
  - **System-level COMET Score**: _0.16_

- **French**:

  - **Average COMET Score (from individual scores)**: _0.14_
  - **System-level COMET Score**: _0.14_

- **Spanish**:
  - **Average COMET Score (from individual scores)**: _0.25_
  - **System-level COMET Score**: _0.25_
