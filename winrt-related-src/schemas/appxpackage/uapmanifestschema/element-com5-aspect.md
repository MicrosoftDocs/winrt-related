---
title: com5:Aspect
description: Specifies the desired data or view aspect of the object when drawing or getting data. (com5:Aspect)
ms.date: 06/22/2023
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
no-loc: [Package, Applications, Application, Extensions, com4:Extension, com4:ComServer, com5:InProcessServer, com5:Class, com5:MiscStatus, com5:Aspect, com5:InProcessHandler, com5:Class, com5:MiscStatus, com5:Aspect, Extensions, com4:Extension, com4:ComServer, com5:InProcessServer, com5:Class, com5:MiscStatus, com5:Aspect, com5:InProcessHandler, com5:Class, com5:MiscStatus, com5:Aspect]
---

# com5:Aspect



Specifies the desired data or view aspect of the object when drawing or getting data.



## Element hierarchy

**[`<Package>`](element-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-1-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:Extension>`](element-com4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:ComServer>`](element-com4-comserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com5:InProcessServer>`](element-com5-inprocessserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com5:Class>`](element-com5-inprocessserver-class.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com5:MiscStatus>`](element-com5-miscstatus.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com5:Aspect>`**  
&nbsp;&nbsp;&nbsp;└─ [`<com5:InProcessHandler>`](element-com5-inprocesshandler.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com5:Class>`](element-com5-inprocesshandler-class.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com5:MiscStatus>`](element-com5-miscstatus.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com5:Aspect>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-1-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:Extension>`](element-com4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:ComServer>`](element-com4-comserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com5:InProcessServer>`](element-com5-inprocessserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com5:Class>`](element-com5-inprocessserver-class.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com5:MiscStatus>`](element-com5-miscstatus.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com5:Aspect>`**  
&nbsp;&nbsp;&nbsp;└─ [`<com5:InProcessHandler>`](element-com5-inprocesshandler.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com5:Class>`](element-com5-inprocesshandler-class.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com5:MiscStatus>`](element-com5-miscstatus.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com5:Aspect>`**  

## Syntax
```syntax
<com5:Aspect     Type = "Content" | "Thumbnail" | "Icon" | "DocPrint"
    OleMiscFlag = An integer value in the range of 0-4194303.
></com5:Aspect>
```


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| Type | The string value for the view aspect of the object. | One of the following values: "Content" , "Thumbnail" , "Icon" , "DocPrint"| Yes |
| OleMiscFlag | The integer value for the view aspect of the object. | An integer value in the range of 0-4194303.| Yes |

### Parent elements

| Parent element | Description |
|-|-|
| [MiscStatus](element-com5-miscstatus.md) | Specifies how to create and display an object. |

## Requirements

| Item | Value |
| ---------------| -------------------------------------------------------------|
| com5 | `http://schemas.microsoft.com/appx/manifest/com/windows10/5` |
| **Minimum OS Version** | Windows 11 version 21H2 (Build 22000) |
