#!/usr/bin/env python

import csv
import math
import rospy
from collections import OrderedDict
from messages.msg import LearningData
import rospkg

class IllnessIdentifier:

    def __init__(self):
        self.status_dict_list = []
        self.features = []
        self.gains = {}
        
        rospack = rospkg.RosPack()

        self.path = rospack.get_path('illness_identifier')
        self.path = self.path + "/src/DataAccessNodeData.csv"
    
    '''------------------------------ Entropy ---------------------------'''

    # Calculates the entropy of the given data set for the target attribute.
    def entropy(self, data, target_attr):
    
        val_freq = {}
        data_entropy = 0.0
        
        # Calculate the frequency of each of the values in the target attr
        for record in data:
            if (record[target_attr] in val_freq):
                val_freq[record[target_attr]] += 1.0
            else:
                val_freq[record[target_attr]]  = 1.0
    
        # Calculate the entropy of the data for the target attribute
        for freq in val_freq.values():
            data_entropy += (-freq/len(data)) * math.log(freq/len(data), 2) 
    
        return data_entropy

    '''------------------------------ Information Gain ---------------------------'''

    # Calculates the information gain (reduction in entropy) that
    #   would result by splitting the data on the chosen attribute (attr).

    def gain(self, data, attr, target_attr):
    
        val_freq = {}
        subset_entropy = 0.0
    
        # Calculate the frequency of each of the values in the target attribute
        for record in data:
            if (record[attr] in val_freq):
                val_freq[record[attr]] += 1.0
            else:
                val_freq[record[attr]]  = 1.0
    
        # Calculate the sum of the entropy for each subset of records weighted by their probability of occuring in the training set.
        for val in val_freq.keys():
            val_prob = val_freq[val] / sum(val_freq.values())
            data_subset = [record for record in data if record[attr] == val]
            subset_entropy += val_prob * self.entropy(data_subset, target_attr)
    
        # Subtract the entropy of the chosen attribute from the entropy of the whole data set with respect to the target attribute (and return it)
        return (self.entropy(data, target_attr) - subset_entropy)

    '''------------------------------ Receive Data Callback --------------------'''

    #ROS Callback for subscriber
    '''
    - Here we have to define another way to structure (LearningData.msg must be changed)
    - structure of status_dict_list:
        [OrderedDict(), OrderedDict(),...]
        -> Each OrderedDict() contains one entry of each type of module (defined in features)
    - Data must come this way (how?)
    - Do we persist in a .csv or keep it this way?
    - Check DataAccessNode to decide how to do it!
    
    ***************** Problems may be solved! (need testing) *****************
    '''
    def receiveData(self):
        try:
            with open(self.path) as f:
                read = csv.reader(f)
                self.features = next(read)
                i = 0
            with open(self.path) as f:
                reader = csv.DictReader(f)
                self.status_dict_list = [r for r in reader]
            
            target_attr = self.features[-1]
            data = self.status_dict_list
            attr = self.features

            ent = self.entropy(data, target_attr)
            print("\n\n--------------------------------------------------------------")
            print("Shannon's Entropy of class '"+self.features[-1]+"': ",ent)
            print("--------------------------------------------------------------\n")
            
            for item in range(0, len(attr)-1):
        ##        gain(self.status_dict_list, self.features[item], self.features[-1])
                print(attr[item]+"'s information gain:",self.gain(data, attr[item], target_attr))
                item+=1
            print("\n------------------------------------------------------------\n")
        except:
            print("Cannot open csv file")

    '''------------------------------ Listener ---------------------------------'''

    #ROS Subscriber

    def listener(self):
        rospy.init_node("illness_identifier")
        loop_rate = rospy.Rate(0.01)
        loop_rate.sleep()
        while not rospy.is_shutdown():
            self.status_dict_list = []
            self.features = []
            self.gains = {}
            self.receiveData()
            loop_rate.sleep()

'''------------------------------ Main ---------------------------'''

if __name__ == '__main__':

    illness_identifier = IllnessIdentifier()
    
    illness_identifier.listener()