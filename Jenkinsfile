pipeline{
	agent any
	
	stages{
		stage('prepair'){
			steps{
				echo 'start download'
				sh 'apt-get install qemu-system-arm'
				echo 'end download'
			}
		}
		stage('build'){
			steps{
				echo 'start build'
				echo 'end build'
			}
		}
	}
}