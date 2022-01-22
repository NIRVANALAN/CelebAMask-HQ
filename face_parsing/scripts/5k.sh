# CUDA_VISIBLE_DEVICES=$1 
dsize=5000
python -u main.py --batch_size 8 --imsize 512 --version parsenet \
--train_split_size $dsize \
--total_step 250000 \
--log_path logs/5k \
--version v0.1 \
--model_save_path ./models/$dsize \