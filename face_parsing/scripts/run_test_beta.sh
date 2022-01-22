# python -u main.py --batch_size 4 --imsize 512 \
# --version parsenet --train False \
# --test_image_path ./Data_preprocessing/test_img \
# --test_label_path ./Data_preprocessing/test_results \
# --test_color_label_path ./Data_preprocessing/test_visualize_results \
# --log_path
# --batch_size 1 \
# --test_size 1
# CUDA_VISIBLE_DEVICES=


# #  
# model_save_path=$1
# model_name=$2
# python -u main.py --batch_size 16 --imsize 512 \
# --version parsenet --train False \
# --log_path ./models/$dsize/test_log \
# --model_save_path $model_save_path \
# --model_name $model_name \
# --test_label_save_path eval/auto_vis \
# --test_color_label_save_path eval/auto_label \
# --test_image_path /mnt/lustre/yslan/Dataset/CVPR22/CelebAMaskFormat/train_img \
# --test_label_path /mnt/lustre/yslan/Dataset/CVPR22/CelebAMaskFormat/train_label \


# large BS for test
python -u main.py --batch_size 48 --imsize 512 --version parsenet \
--train False \
--pretrained_model model \
--model_save_path models \
--version parsenet \

# --model_save_path ./models/autoshot_all_v2 \
# --img_path /mnt/lustre/yslan/Dataset/CVPR22/CelebAMaskFormat/train_img \
# --label_path /mnt/lustre/yslan/Dataset/CVPR22/CelebAMaskFormat/train_label \
# --img_suffix .jpg