model_save_path=./models/$dsize
dsize=1000
python -u main.py --batch_size 8 --imsize 512 --version parsenet \
--train_split_size $dsize \
--total_step 250000 \
--log_path logs/1k \
--version v0.1 \
--model_save_path $model_save_path \
--eval_step 10 \
--sample_step 5
