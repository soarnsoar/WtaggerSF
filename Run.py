import os
from Configuration import conf
import optparse

if __name__ == '__main__':
   usage = 'usage: %prog [options]'
   parser = optparse.OptionParser(usage)
   

   parser.add_option("-y","--year",   dest="year", help="year")
   parser.add_option("-w","--wp",   dest="wp", help="wtagger wp")
   parser.add_option("-b","--bin",   dest="bin", help="bin")
   (options, args) = parser.parse_args()

   year=options.year
   wp=options.wp
   bin=options.bin
  
   ##--carddir
   carddir=conf[year][wp]['carddir']
   carddirname=carddir.rstrip('/').split('/')[-1]
   
   #
   #BIN='200_300'
   #combineCards.py -S PASS=Datacards/___${BIN}__PassDeepAK8WP5/FatJet_msoftdrop_nom/datacard.txt TOTAL=Datacards/___${BIN}/FatJet_msoftdrop_nom/datacard.txt > ${BIN}.txt
   curdir=os.getcwd()

   workdir='/'.join([year,wp,bin])
   os.system('mkdir -p '+workdir)
   os.chdir(year+'/'+wp)
   ##--
   if not os.path.isdir(carddirname):
       #os.system('rm -rf '+carddirname)
       os.system('cp -r '+carddir+' .')

   os.chdir(curdir+'/'+workdir)
   carddir_relpath='../'+carddirname

   ##
   variable=conf[year][wp]['variable']
   bins=conf[year][wp]['bins'][bin]
   
   argument=''
   for b in bins:
      binname=bins[b]
      argument+=' '+b+'='+carddir_relpath+'/'+binname+'/'+variable+'/datacard.txt'
       

   combinecard='combineCards.py -S '+argument+' > combined.txt'
   print "---combine cards---"
   print combinecard
   
   os.system(combinecard)


   ##---Make Workspacke
   makeworkspace='text2workspace.py combined.txt -P HiggsAnalysis.CombinedLimit.HiggsCombinePhysicsModel.HighMassScalar.DeepAK8SF:EvalDeepAK8SF'
   print '----make workspace---'
   print makeworkspace
   os.system(makeworkspace)


   '''
   robust="--robustFit 1"

   combineTool.py -d 200_300.root -M Impacts -m 1000 --doInitialFit $robust
   combineTool.py -d 200_300.root -M Impacts -m 1000 --doFits $robust
   combineTool.py -d 200_300.root -M Impacts -m 1000 -o impacts.json
   plotImpacts.py -i impacts.json -o impacts

   '''
   ##----Impact plot
   print "--run impact plot"
   drawimpact='\
   combineTool.py -d combined.root -M Impacts -m 1000 --doInitialFit --robustFit 1;\
   combineTool.py -d combined.root -M Impacts -m 1000 --doFits --robustFit 1;\
   combineTool.py -d combined.root -M Impacts -m 1000 -o impacts.json;\
   plotImpacts.py -i impacts.json -o impacts;\
   '
   os.system(drawimpact)
