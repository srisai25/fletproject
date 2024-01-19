import pefile 
import re


def header_guy(patho):
    pe=pefile.PE(patho)
    mahadicto={}

    for i in pe.DOS_HEADER.dump():
        init_split=re.split("[\s\t]",i)
        order=[w for w in init_split if(len(w)>1)]
        try:
            temp=order[2]
            ns=""
            for i in temp:
                if(i.isalnum()):
                    ns+=i

            mahadicto.update({ns[0]+"_"+ns[1:]:int(order[3],16)})
        except:
            pass

    for i in pe.FILE_HEADER.dump():
        init_split=re.split("[\s\t]",i)
        order=[w for w in init_split if(len(w)>1)]
        try:
            temp=order[2]
            ns=""
            for i in temp:
                if(i.isalnum()):
                    ns+=i

            mahadicto.update({ns:int(order[3],16)})

        except:
            pass

    for j in pe.OPTIONAL_HEADER.dump():
        init_split=re.split("[\s\t]",j)
        order=[w for w in init_split if(len(w)>1)]

        try:
            temp=order[2]
            ns=""
            for i in temp:
                if(i.isalnum()):
                    ns+=i

            mahadicto.update({ns:int(order[3],16)})

        except:
            pass
    
        section_entro=[]
        characteristics=[]

        for i in pe.sections:
            w=i.get_entropy()
            section_entro.append(w)
            characteristics.append(i.Characteristics)

        #print(section_entro)
        #print(characteristics)
        
        mahadicto.update({"SectionMinEntropy":min(section_entro)})
        mahadicto.update({"SectionMaxEntropy":max(section_entro)})
        mahadicto.update({"SectionMaxChar":max(characteristics)})
        
    #for i in mahadicto.items():
        #print(i[0]," ",i[1])

    return mahadicto

#header_guy(r"C:\Users\admin\Downloads\donottouch\virus1.exe")
