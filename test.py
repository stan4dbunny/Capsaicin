import flip_evaluator as flip
import matplotlib.pyplot as plt
import glob
import csv
import locale
if __name__ == '__main__':

    ref = "dump/sponza_reflection_noSSR_13/Pt_Sponza_User_Reflection_1276_0.040956.png"
    test = "dump/sponza_reflection_noSSR_13/SingleBounce_Sponza_User_Reflection_1350_0.016731Reflection.png"
    
    flipErrorMap, meanFLIPError, parameters = flip.evaluate(ref, test, "LDR")
    plt.imsave("dump/sponza_reflection_noSSR_13/"+"Singlebounce"+"_"+str(round(meanFLIPError, 6))+".png", flipErrorMap)
    #files = glob.glob ("dump/*.jpeg")
        
    #for myFile in files:
    #    flipErrorMap, meanFLIPError, parameters = flip.evaluate(ref, myFile, "HDR")
        #print("Mean FLIP error: ", round(meanFLIPError, 6), "\n")
        
    #    plt.imshow(flipErrorMap)

        #writer.writerow(numbers)
    #    plt.savefig("dump/"+fileName+"_"+str(round(meanFLIPError, 6))+".jpeg")
    #with open('flipresults.csv', 'w', newline='') as file:
    #    writer = csv.writer(file)
    #    writer.writerow(["Step Size","Sun Step Size","Density Threshold","Mean Error"])
    #    
    

    # reference_files = glob.glob("dump/ref/*.png")
    # test_files = glob.glob("dump/test/*.png")

    # for ref in reference_files:
    #     for test in test_files:
    #         test_string = test.split("test")[1].split("\\")[1].split("GI-1.1")[0].strip("_")
    #         if ref.__contains__(test_string):
    #             flipErrorMap, meanFLIPError, parameters = flip.evaluate(ref, test, "LDR")
    #             plt.imsave("dump/results/"+test_string+"_"+str(round(meanFLIPError, 6))+".png", flipErrorMap)

    
    


