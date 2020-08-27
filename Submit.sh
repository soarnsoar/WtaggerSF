
#   parser.add_option("-c","--command",   dest="command", help="command to run")
#   parser.add_option("-d","--workdir",   dest="workdir", help="workarea")
#   parser.add_option("-n","--jobname",   dest="jobname", help="jobname")
#   parser.add_option("-m","--ncpu",   dest="ncpu", help="number of multicores",default=1)
#   parser.add_option("-s","--submit",   dest="submit",action="store_true", help="submit",default=False)


Years=(2016 2017 2018)
WPs=(DeepAK8WP1)
Bins=(200_300 300_400 400_800)
CURDIR=${PWD}
for Year in ${Years[@]};do
    for WP in ${WPs[@]};do
	for Bin in ${Bins[@]};do
	    command="cd ${CURDIR}&&python Run.py -y ${Year} -w ${WP} -b ${Bin}"
	    workdir="workdir__${Year}__${WP}__${Bin}"
	    jobname="SF__${Year}__${WP}__${Bin}"
	    echo "python python_tool/ExportShellCondorSetup.py -c ${command} -d ${workdir} -n ${jobname} -m 1 -s"
	    python python_tool/ExportShellCondorSetup.py -c "${command}" -d "${workdir}" -n "${jobname}" -m 1 -s
	done
    done
done
