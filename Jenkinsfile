pipeline{
	agent any
	
	stages{
		stage('download_openbmc_image'){
			steps{
				echo 'start download'
				sh 'wget --progress=bar:force https://jenkins.openbmc.org/job/ci-openbmc/lastSuccessfulBuild/distro=ubuntu,label=docker-builder,target=romulus/artifact/openbmc/build/tmp/deploy/images/romulus/*zip*/romulus.zip'
 				sh 'unzip romulus.zip'
 				echo 'end download'
			}
		}
		stage('build'){
			steps{
				echo 'start build'
				sh 'qemu-system-arm -m 256 -M romulus-bmc -nographic -drive file=romulus/obmc-phosphor-image-romulus-20250212052422.static.mtd,format=raw, if=mtd -net nic -net user,hostfwd=:0.0.0.0:2222-:22,hostfwd=:0.0.0.0:2443-:443,hostfwd=udp:0.0.0.0:2623-:623,hostname=qemu -daemonize'
				echo 'end build'
			}
		}
		stage('tests'){
			steps{
				echo 'start tests'
				echo 'end tests'
			}
		}
	}
}