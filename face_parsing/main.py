from parameter import *
import ipdb
from trainer import Trainer
from tester import Tester
from data_loader import Data_Loader
from torch.backends import cudnn
from utils import make_folder


def main(config):
    # For fast training
    cudnn.benchmark = True

    eval_loader = Data_Loader(
        config.test_image_path,
        config.test_label_path,
        config.imsize,
        config.batch_size,
        # config.train,
        False,
        config.test_size,
        'jpg' # test, jpg; train png
    )

    if config.train:

        # Create directories if not exist
        make_folder(config.model_save_path, config.version)
        make_folder(config.sample_path, config.version)
        make_folder(config.log_path, config.version)

        data_loader = Data_Loader(
            config.img_path,
            config.label_path,
            config.imsize,
            config.batch_size,
            config.train,
            config.train_split_size,
            config.img_suffix,
        )


        trainer = Trainer(data_loader.loader(), eval_loader.loader(), config)
        trainer.train()
    else:
        # tester = Tester(config)
        # tester.test()
        trainer = Trainer(None, eval_loader.loader(), config)
        trainer.eval()


if __name__ == "__main__":
    config = get_parameters()
    print(config)
    main(config)
