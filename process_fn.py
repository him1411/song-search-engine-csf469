def process_function(query):
    main_class.queryStr = query
    main_class.terminal_function()
    
    #find max wala function#######################
    with open('savers/store.json') as json_data:
        score = json.load(json_data)
    sorted_score = sorted(score, key=score.get, reverse=True)
    docFiles = [f for f in os.listdir('./corpus') if f.endswith(".html")]
    docFiles.sort()
    for i in sorted_score[:10]:
        print(i)

    #end of find max################################

    linkNumber_list = sorted_score[:10]
    docList = {}
    f = open("linksCorpus.txt")
    data = f.read()
    data = data.split("\n")
    '''
    print(linkNumber_list)
    for linkNum in linkNumber_list:
        docList.append(data[int(linkNum)]);
    print(docList)
    '''
    docList['D1'] = '1.html'
    docList['D2'] = '2.html'
    return docList