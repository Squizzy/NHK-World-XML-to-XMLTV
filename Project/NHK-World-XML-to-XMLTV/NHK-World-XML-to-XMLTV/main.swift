//
//  main.swift
//  NHK-World-XML-to-XMLTV
//
//  Created by Guillaume on 31/01/2017.
//  Copyright © 2017 CrazySquirrel. All rights reserved.
//

import Foundation

print("Hello, World!")

let inputFile = "convertjson.xml"
let outputFile = "finalXML.xmltv"
// let text = "some1 text" //just a text
var inputXML = String()

if let dir = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first {
    
    let inputPath = dir.appendingPathComponent(inputFile)
    //reading
    do {
         inputXML = try String(contentsOf: inputPath, encoding: String.Encoding.utf8)
    //    print("read from file: \(inputXML)")
    }
    catch {
        print("Error reading the file: \(inputFile) - message: \(error.localizedDescription)")
        /* error handling here */}

    print("read from file: \(inputXML)")

let outputPath = dir.appendingPathComponent(outputFile)
    let p=1
    //writing
    if p==1 {
        do {
            try inputXML.write(to: outputPath, atomically: true, encoding: String.Encoding.utf8)
        }
        catch {
            print("Error writing the file: \(inputFile) - message: \(error.localizedDescription)")
            /* error handling here */}
    }
}
