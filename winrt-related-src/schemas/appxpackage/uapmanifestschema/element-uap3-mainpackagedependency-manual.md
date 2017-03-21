---
Description: Specifies the main app package to which this supplemental package applies.
Search.Product: eADQiWindows 10XVcnh
title: uap3:MainPackageDependency (Windows 10)
ms.assetid: 8de4b12b-0f0d-48d0-b3ff-28aae81fb13c
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
---

# uap3:MainPackageDependency (Windows 10)


Specifies the main app package to which this supplemental package applies.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-dependencies.md">&lt;Dependencies&gt;</a></dt>
<dd><b>&lt;uap3:MainPackageDependency&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax


```
<uap3:MainPackageDependency Name = A string between 3 and 50 characters in
                                   length that consists of alpha-numeric, 
                                   period, and dash characters. >
</uap3:MainPackageDependency>
```

## Attributes and Elements


**Attributes**

| Attribute | Description                                                                                                                     | Data type                                                                                                   | Required | Default value |
|-----------|---------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|----------|---------------|
| **Name**  | The name as it appears in the **Name** attribute of the [**Identity**](element-identity.md) element of the dependency package. | A string between 3 and 50 characters in length that consists of alpha-numeric, period, and dash characters. | Yes      |               |

 

**Child Elements**

None.

**Parent Elements**

| Parent Element                               | Description                                                                 |
|----------------------------------------------|-----------------------------------------------------------------------------|
| [**Dependencies**](element-dependencies.md) | Declares other packages that a package depends on to complete its software. |

 

## Examples


```XML
<Package ...
         xmlns:uap3="http://schemas.microsoft.com/appx/manifest/uap/windows10/3"  
         IgnorableNamespaces="... uap3">
    <Dependencies>  
        <TargetDeviceFamily Name="Windows.Universal" MinVersion="11.0.0.0" 
                            MaxVersionTested="12.0.0.0"/>  
        <uap3:MainPackageDependency Name="MyApp.Main"/>  
    </Dependencies>  
</Package>
```

## Requirements


|               |                                                            |
|---------------|------------------------------------------------------------|
| **Namespace** | http://schemas.microsoft.com/appx/manifest/uap/windows10/3 |

 

 

 



