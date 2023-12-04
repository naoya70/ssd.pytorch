import sys
sys.path.append('/content/ssd.pytorch/layers/functions')
from .detection import Detect
from .prior_box import PriorBox


__all__ = ['Detect', 'PriorBox']
