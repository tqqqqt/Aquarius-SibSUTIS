pipeline{
	agent any
	
	stages{
		stage('prepair'){
			steps{
				echo 'start download'
				sh 'whoami'
				sh 'ls'
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