from qgis.core import QgsProject
import csv

mapcanvas = iface.mapCanvas()

layers = mapcanvas.layers()

inputlayer = QgsProject.instance().mapLayersByName('Tways_LocalRoutes_TOD13_ShapesConnected_UTM')[0]
itlayer = QgsProject.instance().mapLayersByName('Merged_Stops_TOD13_UTM')[0]
dist = 10

def selectPointsInBuffer(inputlayer, itlayer, dist):
    #with open('/Users/hemarayaprolu/Dropbox (Sydney Uni)/Analysis/Historic_Bus_GTFS/AutomateDigitising/1925/StopsByRoute.csv', 'w', encoding = 'utf-8') as out:
    with open('/Users/hemarayaprolu/Dropbox (Sydney Uni)/Analysis/iMove : Liverpool Project/CoreNetwork_CurrentAndProposed/GTFS/Stops/StopsByRoute_TwayLocalRotues_TOD13.csv', 'w', encoding = 'utf-8') as out:
    #with open('/Users/hemarayaprolu/Dropbox (Sydney Uni)/Analysis/iMove : Liverpool Project/Middleton Grange/GTFS_v1/stopsByRoute.csv', 'w', encoding = 'utf-8') as out:
        outputwriter = csv.writer(out, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        idx = itlayer.fields().indexFromName("stop_id")
        header = [field.name() for field in inputlayer.fields()] + ['stop_id']
        outputwriter.writerow(header)
        #iterate over feature of inputlayer and get geometry
        for feat in inputlayer.getFeatures():
            itlayer.removeSelection()
            geom = feat.geometry()
            #iterate over feature of itlayer and get geometry
            for itfeat in itlayer.getFeatures():
                itgeom = itfeat.geometry()
                #test if geom of itlayer is in the buffer of inputlayer, if yes select the feature 
                if geom.singleSidedBuffer(dist,10, 0).contains(itgeom):
                    itlayer.select(itfeat.id())
            for sfeat in itlayer.selectedFeatures():
                #attrs = sfeat.attributeMap()
                value_fields = [feat['shape_id'],feat['begin'],feat['end']] + [sfeat.attributes()[idx]]
                outputwriter.writerow(value_fields)
                pass
    

selectPointsInBuffer(inputlayer, itlayer, dist)