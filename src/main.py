from compute_pda import main

def welcome():
    print("\033c", end="")
    print('''
                `7MMF'  `7MMF'MMP""MM""YMM `7MMM.     ,MMF'`7MMF'      
                  MM      MM  P'   MM   `7   MMMb    dPMM    MM        
                  MM      MM       MM        M YM   ,M MM    MM        
                  MMmmmmmmMM       MM        M  Mb  M' MM    MM        
                  MM      MM       MM        M  YM.P'  MM    MM      , 
                  MM      MM       MM        M  `YM'   MM    MM     ,M 
                .JMML.  .JMML.   .JMML.    .JML. `'  .JMML..JMMmmmmMMM 
                                                                                                                                       
  .g8"""bgd `7MMF'  `7MMF'`7MM"""YMM    .g8"""bgd `7MMF' `YMM' `7MM"""YMM  `7MM"""Mq.  
.dP'     `M   MM      MM    MM    `7  .dP'     `M   MM   .M'     MM    `7    MM   `MM. 
dM'       `   MM      MM    MM   d    dM'       `   MM .d"       MM   d      MM   ,M9  
MM            MMmmmmmmMM    MMmmMM    MM            MMMMM.       MMmmMM      MMmmdM9   
MM.           MM      MM    MM   Y  , MM.           MM  VMA      MM   Y  ,   MM  YM.   
`Mb.     ,'   MM      MM    MM     ,M `Mb.     ,'   MM   `MM.    MM     ,M   MM   `Mb. 
  `"bmmmd'  .JMML.  .JMML..JMMmmmmMMM   `"bmmmd'  .JMML.   MMb..JMMmmmmMMM .JMML. .JMM.                               
        ''')
    
if __name__ == "__main__":
    welcome()
    main()
