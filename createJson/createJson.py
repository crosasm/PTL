#!/usr/bin/python

import sys
import csv
import json

def read_text(input_text_file):

    file_data = {}    
    text_data = open(input_text_file)
    lines = text_data.readlines()[1:]
    for line in lines:
        line_pieces = line.split('||')
        id_line = line_pieces[0]
        line_content = line_pieces[1][:-1]
        file_data[id_line] = {'text': line_content}
    return file_data


def read_attributes(input_attrib_file, temp_text_data, type_dataset):
    
    attributes = open(input_attrib_file)
    #with open(input_attrib_file) as attributes:
    #   rd = csv.DictReader(attributes, delimiter=',')
    #   for row in rd:
    #       print(row) 

    lines = attributes.readlines()[1:]
    for line in lines:
        if (type_dataset == 'test'):
            #print("PREDICTION: ", type_dataset)
            id_variant, gene, variant = line.split(',')
            text = temp_text_data[id_variant]['text']
            temp_text_data[id_variant] = {'text': text, 
                                          'gene': gene, 
                                          'variation': variant[:-1]}
        else: 
            #print("TRAINING: ", type_dataset)
            id_variant, gene, variant, v_class = line.split(',')
            text = temp_text_data[id_variant]['text']
            temp_text_data[id_variant] = {'text': text, 
                                         'gene': gene, 
                                         'variation': variant, 
                                         'class': v_class[:-1]}
    return temp_text_data


def main():
    
    files_to_be_read = str(sys.argv)
    # print(files_to_be_read)
    
    if (len(sys.argv) == 5):   
        
        type_dataset = sys.argv[4]
        temp_file_data = {}
        text_to_be_read = sys.argv[1]
        # print(text_to_be_read)
    
        temp_text_data = read_text(text_to_be_read)
        # print(temp_text_data)
        
        attributes_to_be_read = sys.argv[2]

        temp_text_data = read_attributes(attributes_to_be_read, temp_text_data, 
                         type_dataset)
        #print(temp_text_data)

        output_json = sys.argv[3]
        #print(output_json)
        with open(output_json, "w") as write_file:
           for record in temp_text_data.values():
               json.dump(record, write_file)
               write_file.write("\n") # Add newline because PyJSON does not
    else:

        print("Two files required to be merged in a json")


if __name__ == "__main__":
    main()
