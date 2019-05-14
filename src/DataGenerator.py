import numpy as np
from Initialization import initClasses

def generateData(numberOfClasses, numberOfFeatures, numberOfRecordsPerClass,
                 featureMeanRange, randomNumberSeed, trueNumberOfClasses=None):

    if trueNumberOfClasses == None:
        trueNumberOfClasses = numberOfClasses

    TOTAL_NUMBER_OF_RECORDS = numberOfClasses * numberOfRecordsPerClass
    
    featureDistributionData = initClasses(trueNumberOfClasses, numberOfFeatures,
                                            featureMeanRange,
                                            randomNumberSeed=randomNumberSeed)
    
    if trueNumberOfClasses == None:
        classIdx = list(range(numberOfClasses))
    else:
        classIdx = np.random.choice(trueNumberOfClasses, numberOfClasses)
    # Initialize data nxp
    data = np.empty((TOTAL_NUMBER_OF_RECORDS, numberOfFeatures))
    for i in range(numberOfClasses):
        idx = classIdx[i]
        generatedFeatures = np.random.multivariate_normal(featureDistributionData[idx].featureMeans,
                                                        featureDistributionData[idx].featureCovariances,
                                                        size=(numberOfRecordsPerClass))

        rowRangeForCurrentClass = range(i*numberOfRecordsPerClass,(i+1)*numberOfRecordsPerClass)                                                        
        data[rowRangeForCurrentClass,:] = generatedFeatures
    
    labels = list(range(numberOfClasses))
    labelsArray = np.repeat(labels, numberOfRecordsPerClass)
    
    #Shuffle with labels
    concatenatedData = np.concatenate((data,labelsArray[:,np.newaxis]), axis=1)
    np.random.shuffle(concatenatedData)
    
    data = concatenatedData[:,:-1]
    labelsArray = concatenatedData[:,-1]
    
    return (data, labelsArray)

if __name__ == "__main__":
    
    NUMBER_OF_CLASSES = 4
    NUMBER_OF_FEATURES = NUMBER_OF_CLASSES*2
    NUMBER_OF_FEATURES_PER_CLASS = 200
    TOTAL_NUMBER_OF_RECORDS = NUMBER_OF_CLASSES * NUMBER_OF_FEATURES_PER_CLASS
        
    FEATURE_MEAN_RANGE = [0, 50]
        
    RANDOM_NUMBER_SEED = 0
    
    data, labels = generateData(NUMBER_OF_CLASSES, NUMBER_OF_FEATURES,
                                NUMBER_OF_FEATURES_PER_CLASS, FEATURE_MEAN_RANGE,
                                RANDOM_NUMBER_SEED)
