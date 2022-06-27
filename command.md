# train
> python train.py --img 640 --data iris.yaml --cfg yolov5n.yaml --weights yolov5n.pt --batch 24 --epochs 10

# export ONNX
python export.py --weights yolov5s.pt --include torchscript onnx
python -m onnxsim yolov5s.onnx yolov5s-sim.onnx