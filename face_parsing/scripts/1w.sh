# CUDA_VISIBLE_DEVICES=$1 
dsize=10000
python -u main.py --batch_size 8 --imsize 512 \
--train_split_size $dsize \
--model_save_path ./models/$dsize \
--train_split_size $dsize \
--total_step 500000 \
--log_path logs/1w \
--version v0.1 \