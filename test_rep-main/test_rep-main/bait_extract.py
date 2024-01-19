import pefile 


def feat_ex(s):
    pe_obj=pefile.PE(s)
    #print(pe_obj)
    main_feat={}

    '''
    for i in pe_obj.DOS_HEADER.dump():
        print(i)
    '''

    #for j in pe_obj.OPTIONAL_HEADER.dump():
        #print(j)

    main_feat.update({"size_of_data":float(int(hex(pe_obj.OPTIONAL_HEADER.SizeOfInitializedData),16))})

    c=0
    for k in pe_obj.sections:
        main_feat.update({"virtual_address":float(int(hex(k.VirtualAddress),16))})
        main_feat.update({"virtual_size":float(int(hex(k.Misc_VirtualSize),16))})
        main_feat.update({"entropy":k.get_entropy()})
        
        if(c==0):
            break

    print(main_feat)

    return main_feat
        
