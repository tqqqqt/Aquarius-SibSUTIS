pipeline{
	agent{
		node{
			label 'jens-qemu'
		}
	}
	environment{ }
	stages{
		stage('prepair'){
			steps{
				sh 'start download'
				//sh 'sudo apt install qemu-system-arm'
				sh 'end download'
			}
		}
		stage('build'){
			steps{
				sh 'start build'
				sh 'end build'
			}
		}
	}
}