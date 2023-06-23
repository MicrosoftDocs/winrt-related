---
title: com5:Aspect
description: Specifies the desired data or view aspect of the object when drawing or getting data. (com5:Aspect)
ms.date: 06/22/2023
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com5:Aspect



## Description

Specifies the desired data or view aspect of the object when drawing or getting data.



## Element Hierarchy
[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp; [\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [\<com5:Class\> (in InProcessServer)](element-com5-inprocessserver-class.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [\<MiscStatus\>](element-com5-miscstatus.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;  **&lt;com5:Aspect&gt;**

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [\<com5:Class\> (in InProcessHandler)](element-com5-inprocesshandler-class.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [\<MiscStatus\>](element-com5-miscstatus.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;  **&lt;com5:Aspect&gt;**


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

| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com5 | http://schemas.microsoft.com/appx/manifest/com/windows10/5 |
