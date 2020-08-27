robust="--robustFit 1"

combineTool.py -d 200_300.root -M Impacts -m 1000 --doInitialFit $robust
#combineTool.py -d 200_300.root -M Impacts -m 1000  $robust --doFits
combineTool.py -d 200_300.root -M Impacts -m 1000 --doFits $robust
combineTool.py -d 200_300.root -M Impacts -m 1000 -o impacts.json

plotImpacts.py -i impacts.json -o impacts
