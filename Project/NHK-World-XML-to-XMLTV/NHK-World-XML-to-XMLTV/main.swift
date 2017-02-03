//
//  main.swift
//  NHK-World-XML-to-XMLTV
//
//  Created by CrazySquirrel (Squizzy) on 31/01/2017.
//  Copyright © 2017 CrazySquirrel. All rights reserved.
//

import Foundation


//////
//      origXMLItem:     Class for the original file XML
//      origXMLGenre:    Class of genres
/////

class origXMLItem {
    var seriesId:Int?
    var airingId:Int?
    var title:String?
    var desc:String?
    var link:String?
    var pubDate:Double = 0
    var jstrm:Int?
    var wstrm:Int?
    var vodReserved:Bool = false
    var endDate:Double = 0
    var subtitle:String?
    var content:String?
    var content_clean:String?
    var thumbnail:String?
    var thumbnail_s:String?
    var showlist:Int?
    var internalTag:Int?
    var genre = [origXMLGenre]()
    var analytics:String?
}

class origXMLGenre {
    var TV:Int?
    var Top:Int?
    var LC:Int?
}

//////
//      getDate     converts unix time format to required time format (after adjusting number)
//      @ timezone: +1h = 0100, +2.5h = 0250, -6 = -0600
//      @ length:   0 = short (YYYYMMDD], other = full [YYYYMMDDhhmmss zzzzz] (zzzzz is timezone, first digit may be "-")
//      output:     String containing the date
/////

func getDate(unixDate: Int, timezone: String, length: Int) -> String {
    var finalDateString=""
    let adjustedUnixDate = unixDate / 1000
    if adjustedUnixDate == 0 {return "No Date Provided"}
    let date = NSDate(timeIntervalSince1970: TimeInterval(adjustedUnixDate))
    let dayTimePeriodFormatter = DateFormatter()
    if length==0 {
        dayTimePeriodFormatter.dateFormat = "YYYYMMDD"
         finalDateString = dayTimePeriodFormatter.string(from: date as Date)
    } else {
        dayTimePeriodFormatter.dateFormat = "YYYYMMDDhhmmss"
        let dateString = dayTimePeriodFormatter.string(from: date as Date)
        finalDateString = dateString + timezone
    }
    return "\(finalDateString)"
}

///////
//      loadXML:      Read inputFile into a string
//      @ inputFile:  String (eg "inputfile.txt")
//      output:       outputs a String
///////

func loadXML(inputFile:String) -> String {
    var fileText:String = ""

    // path where the files will be found
    if let dir = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first {
        // filename with path
        let inputPath = dir.appendingPathComponent(inputFile)

        do {
            fileText = try String(contentsOf: inputPath, encoding: String.Encoding.utf8)
        }
        catch {
            print("Error reading the file: \(inputFile) - message: \(error.localizedDescription)")
            /* error handling here */
        }
    }
    return fileText
}


///////
//      writeXML:           Write outputContent into outputFile
//      @ outputFile:       String of the file name, eg "Out.txt"
//      @ outputContent:    String containing the content to write into the file
//      output:             None
///////

func writeXML(outputFile:String, outputContent:String) {
    // path where the files will be found
    if let dir = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first {
        let outputPath = dir.appendingPathComponent(outputFile)
        do {
            try outputContent.write(to: outputPath, atomically: true, encoding: String.Encoding.utf8)
        }
        catch {
            print("Error writing the file: \(outputFile) - message: \(error.localizedDescription)")
            /* error handling here */
        }
    }
}

// tester program
print("LoadXML")
let tmpXML = loadXML(inputFile: "convertjson.xml")
print("equate")
if tmpXML.contains("<title>") {
    print("yes, contains <title>")
}
print("writeXML")
writeXML(outputFile: "finalXML1.xmltv", outputContent: tmpXML)
print("Finished")