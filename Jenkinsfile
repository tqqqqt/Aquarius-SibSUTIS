pipeline{
	agent any
	
	stages{
		stage('download_openbmc_image'){
			steps{
				echo 'start download'
				sh 'wget -nv https://jenkins.openbmc.org/job/ci-openbmc/lastSuccessfulBuild/distro=ubuntu,label=docker-builder,target=romulus/artifact/openbmc/build/tmp/deploy/images/romulus/*zip*/romulus.zip'
 				sh 'unzip -o romulus.zip'
 				echo 'end download'
			}
		}
		stage('build'){
			steps{
				echo 'start build'
				script{
					def find_result=sh(
						script: 'find romulus/ -name *.static.mtd',
						returnStdout: true).trim()
					env.FILE_PATH=find_result
					echo "file - ${env.FILE_PATH}"
					def qemu_comand="nohup qemu-system-arm -m 256 -M romulus-bmc -nographic -drive file=${env.FILE_PATH},format=raw,if=mtd -net nic -net user,hostfwd=:0.0.0.0:2222-:22,hostfwd=:0.0.0.0:2443-:443,hostfwd=udp:0.0.0.0:2623-:623,hostname=qemu > qemu.log 2>&1 &"
					echo "comand - ${qemu_comand}"
					sh(qemu_comand)
					sleep 60
				}
				echo 'end build'
			}
		}
		stage('tests'){
			steps{
				echo "start tests"
				sh "pwd"
				sh "ls"
				echo "end tests"
			}
		}
	}
	post{
		always{
			sh "rm -f -r romulus"
			sh "rm -f romulus.zip"
		}
	}
}