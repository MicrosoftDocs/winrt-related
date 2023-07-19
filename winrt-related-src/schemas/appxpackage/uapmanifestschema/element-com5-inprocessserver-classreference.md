---
title: com5:ClassReference (in InProcessServer)
description: Specifies the class or class reference with which the registered in-process server is associated and sets registration details. (com5:InProcessServerClassReference)
ms.date: 06/22/2023
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com5:ClassReference (in InProcessServer)



## Description

Specifies the class or class reference with which the registered in-process server is associated and sets registration details.

## Element Hierarchy
[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp; [\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [\<com4:Extension\>](element-com4-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [\<com4:ComServer\>](element-com4-comserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [\<com5:InProcessServer\>](element-com5-inprocessserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; **&lt;com5:ClassReference&gt;**


## Syntax
```syntax
<com5:ClassReference     ThreadingModel = "Both" | "STA" | "MTA" | "MainSTA" | "Neutral"
    Virtualization = "enabled" | "disabled"
    Id = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
></com5:ClassReference>
```


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| ThreadingModel | The type of threading model supported by the runtime class. | One of the following values: "Both" , "STA" , "MTA" , "MainSTA" , "Neutral"| Yes |
| Virtualization | Specifies whether virtualization is used when loading the class. | One of the following values: "enabled" , "disabled"| Yes |
| Id | The Id of the [Class](element-com4-class.md) being referenced. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.| Yes |

## Parent elements

| Parent element | Description |
|-|-|
| [com5:InProcessServer](element-com5-inprocessserver.md) | Registers an in-process server with one or many class registrations. |

## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com5 | `http://schemas.microsoft.com/appx/manifest/com/windows10/5` |
