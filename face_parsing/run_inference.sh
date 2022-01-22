CUDA_VISIBLE_DEVICES=$1 python -u main.py --batch_size 4 --imsize 512 \
--version parsenet --train False \
--test_image_path ./Data_preprocessing/extra_test_img \
--test_label_path ./Data_preprocessing/extra_test_results \
--test_color_label_path ./Data_preprocessing/extra_test_visualize_results \
--batch_size 1 \
--test_size 1




