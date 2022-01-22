# CUDA_VISIBLE_DEVICES=$1 
python -u main.py --batch_size 8 --imsize 512 --version parsenet \
--model_save_path ./models/autoshot_all_log \
--img_path /mnt/lustre/yslan/Dataset/CVPR22/CelebAMaskFormat/train_img \
--label_path /mnt/lustre/yslan/Dataset/CVPR22/CelebAMaskFormat/train_label \
--img_suffix png \
--log_path logs/autoshot \
--version v0.1 \
--eval_step 2000 \
# --test_image_path /mnt/lustre/yslan/Dataset/CVPR22/CelebAMaskFormat/train_img \
# --test_label_path /mnt/lustre/yslan/Dataset/CVPR22/CelebAMaskFormat/train_label \
# --train_split_size -1





