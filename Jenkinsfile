pipeline{
	agent any
	
	stages{
		stage('download_openbmc_image'){
			steps{
				echo '-----start download-----'
				sh 'wget -nv https://jenkins.openbmc.org/job/ci-openbmc/lastSuccessfulBuild/distro=ubuntu,label=docker-builder,target=romulus/artifact/openbmc/build/tmp/deploy/images/romulus/*zip*/romulus.zip'
 				sh 'unzip -o romulus.zip'
 				echo '-----end download-----'
			}
		}
		stage('build'){
			steps{
				echo '-----start build-----'
				script{
					def find_result=sh(
						script: 'find romulus/ -name *.static.mtd',
						returnStdout: true).trim()
					env.FILE_PATH=find_result
					def qemu_comand="nohup qemu-system-arm -m 256 -M romulus-bmc -nographic -drive file=${env.FILE_PATH},format=raw,if=mtd -net nic -net user,hostfwd=:0.0.0.0:2222-:22,hostfwd=:0.0.0.0:2443-:443,hostfwd=udp:0.0.0.0:2623-:623,hostname=qemu > qemu.log 2>&1 &"
					sh(qemu_comand)
					def exit_flg=1
					while(exit_flg>0){
						def start_qemu=sh(
							script: 'grep -c "romulus login" qemu.log || true',
							returnStdout: true).trim()
						if(start_qemu=="1"){
							exit_flg=0
							break
						}
						else {
							sleep 15
						}
					}
					sleep 40
				}
				echo '-----end build-----'
			}
		}
		stage('python tests'){
			steps{
				echo "-----start tests-----"
				echo "* redfish test:"
				sh "pytest lab5/test_redfish.py --junitxml=reports/result_lab5.xml"
				echo "* web test:"
				sh "pytest lab4/tests.py --junitxml=reports/result_lab4.xml"
				echo "* locust test:"
				sh "locust --headles -f lab6/locustfile.py --host abs -u 10 -r 1 --run-time 60 -E json_posts --csv report/locust"
				echo "-----end tests-----"
			}
		}
	}
	post{
		always{
			archiveArtifacts artifacts: 'report/*.xml', allowEmptyArchive: true, followSymlinks: false, fingerprint: true
			archiveArtifacts artifacts: 'report/*.csv', allowEmptyArchive: true, followSymlinks: false, fingerprint: true
			junit 'report/*.xml'
			junit 'report/*.csv'
			sh "rm -f -r romulus"
			sh "rm -f romulus.zip"
			sh "rm -f qemu.log"
		}
	}
}