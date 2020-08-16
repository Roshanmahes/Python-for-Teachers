grs = ['BalancedTree', 'BullGraph', 'ChvatalGraph', 'CirculantGraph', 'CircularLadderGraph', 'ClawGraph', 'CompleteGraph',
       'CubeGraph', 'CycleGraph', 'DegreeSequence', 'DegreeSequenceExpected', 'DegreeSequenceTree', 'DesarguesGraph',
       'DiamondGraph', 'DodecahedralGraph', 'FlowerSnark', 'FruchtGraph', 'Grid2dGraph', 'GridGraph', 'HeawoodGraph',
       'HexahedralGraph', 'HoffmanSingletonGraph', 'HouseGraph', 'HouseXGraph', 'IcosahedralGraph', 'KrackhardtKiteGraph',
       'LCFGraph', 'LadderGraph', 'LollipopGraph', 'MoebiusKantorGraph', 'OctahedralGraph', 'PappusGraph', 'PathGraph',
       'PetersenGraph', 'RandomBarabasiAlbert', 'RandomGNM', 'RandomGNP', 'RandomHolmeKim', 'RandomLobster', 'RandomRegular',
       'RandomNewmanWattsStrogatz', 'RandomTreePowerlaw', 'StarGraph', 'TetrahedralGraph', 'ThomsenGraph', 'WheelGraph']

examples = {}
for g in grs:
    docs = eval('graphs.' + g + '.__doc__')
    for docline in docs.split('\n'):
        ex_loc = docline.find('graphs.' + g)
        if ex_loc != -1:
            end_paren_loc = docline[ex_loc:].find(')')
            ex_str = docline[ex_loc:end_paren_loc+ex_loc+1]
            ex_str = ex_str.replace('i+','2+')
            ex_str = ex_str.replace('(i','(4')
            break
    try:
        gt2 = eval(ex_str)
        examples[g] = ex_str
    except:
        grs.remove(g)

@interact
def graph_browser(graph_name = selector(grs, label = "Graph type:"), output_type = selector(['2D','3D'])):
    base_g_str = 'graphs.' + graph_name
    docs = eval(base_g_str + '.__doc__')
    doc_ex_loc = docs.find('EXAMPLE')
    if docs.find('PLOTTING') != -1:
        doc_ex_loc = min(doc_ex_loc, docs.find('PLOTTING'))
    print(docs[0:doc_ex_loc])

    t_graph = eval(examples[graph_name])
    if output_type == '2D':
        t_graph.show()
    else:
        t_graph.show3d()
