//
//  main.swift
//  NHK-World-XML-to-XMLTV
//
//  Created by Guillaume on 31/01/2017.
//  Copyright © 2017 CrazySquirrel. All rights reserved.
//

import Foundation

let inputFile = "convertjson.xml"  // the original data file name
let outputFile = "finalXML.xmltv"  // the final data file name

var inputXML = String() // the container for the content of the inputFile
var outputXML = String() // the container for the content for the output file

///////
//    Read inputFile into inputXML
///////
func loadXML() {
    // path where the files will be found
    if let dir = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first {
        // filename with path
        let inputPath = dir.appendingPathComponent(inputFile)
//        print("input path: \(inputPath)")

        do {
            inputXML = try String(contentsOf: inputPath, encoding: String.Encoding.utf8)
        }
        catch {
            print("Error reading the file: \(inputFile) - message: \(error.localizedDescription)")
            /* error handling here */
        }
//    print("read from file: \(inputXML)")
    }
}


///////
//    Write outputXML into outputFile
///////
func writeXML() {
    // path where the files will be found
    if let dir = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first {
        let outputPath = dir.appendingPathComponent(outputFile)
        if 1==1 {
            do {
                try outputXML.write(to: outputPath, atomically: true, encoding: String.Encoding.utf8)
            }
            catch {
                print("Error writing the file: \(inputFile) - message: \(error.localizedDescription)")
                /* error handling here */
            }
        }
    }
}

print("LoadXML")
loadXML()
print("equate")
outputXML = inputXML
if outputXML.contains("<title>") {
    print("yes, contains <title>")
}
print("writeXML")
writeXML()
print("Finished")
