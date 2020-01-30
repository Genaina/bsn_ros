bsn=$PWD

gnome-terminal -x roscore & sleep 5s

################# KNOWLEDGE REPOSITORY #################
gnome-terminal --working-directory=${bsn}/configurations/knowledge_repository -e 'roslaunch data_access.launch' & sleep 1s

################# SYSTEM MANAGER #################
gnome-terminal --working-directory=${bsn}/configurations/system_manager -e 'roslaunch enactor.launch'

################# LOGGING INFRASTRUCTURE #################
gnome-terminal --working-directory=${bsn}/configurations/logging_infrastructure -e 'roslaunch logger.launch' & sleep 1s

################# MANAGED SYSTEM #################
############ INTERFACE ###########
gnome-terminal --working-directory=${bsn}/configurations/target_system -e 'roslaunch probe.launch' & sleep 1s
gnome-terminal --working-directory=${bsn}/configurations/target_system -e 'roslaunch effector.launch' & sleep 1s

############ TARGET SYSTEM ###########
gnome-terminal --working-directory=${bsn}/configurations/target_system -e 'roslaunch g4t1.launch' & sleep 1s
gnome-terminal --working-directory=${bsn}/configurations/target_system -e 'roslaunch g3t1_1.launch' & sleep 1s
gnome-terminal --working-directory=${bsn}/configurations/target_system -e 'roslaunch g3t1_2.launch' & sleep 1s
gnome-terminal --working-directory=${bsn}/configurations/target_system -e 'roslaunch g3t1_3.launch' & sleep 1s
gnome-terminal --working-directory=${bsn}/configurations/target_system -e 'roslaunch g3t1_4.launch' & sleep 1s
gnome-terminal --working-directory=${bsn}/configurations/target_system -e 'roslaunch g3t1_5.launch' & sleep 1s

################# ENVIRONMENT #################
gnome-terminal --working-directory=${bsn}/configurations/environment   -e 'roslaunch patient.launch' & sleep 1s

################# SIMULATION #################
gnome-terminal --working-directory=${bsn}/configurations/simulation -e 'roslaunch analyzer.launch' & sleep 1s
gnome-terminal --working-directory=${bsn}/configurations/simulation -e 'roslaunch injector.launch' & sleep 1s

gnome-terminal --working-directory=${bsn}/configurations/system_manager -e 'roslaunch engine.launch' & sleep 1s
