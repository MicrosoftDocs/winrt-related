---
description: Represents a collection element with the specified attributes that should be added to the applicationHost.config file.
Search.Product: eADQiWindows 10XVcnh
title: serverpreview:CollectionElement
ms.assetid: a6c0f641-661a-407e-9471-2bf1084faa4d


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# serverpreview:CollectionElement


Represents a collection element with the specified attributes that should be added to the applicationHost.config file.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-serverpreview-extension-manual.md">&lt;serverpreview:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-serverpreview-iismodules-manual.md">&lt;serverpreview:IisModules&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-serverpreview-iismodule-manual.md">&lt;serverpreview:IisModule&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-serverpreview-sectiondata-manual.md">&lt;serverpreview:SectionData&gt;</a></dt>
<dd><b>&lt;serverpreview:CollectionElement&gt;</b></dd>
<dl>									
</dd>
</dl>									
</dd>
</dl>									
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax


```
<serverpreview:CollectionElement xsd:anyAttribute>
</serverpreview:CollectionElement>
```

**Key**

          \* optional (zero or more)

## Attributes and Elements


**Attributes**

| Attribute         | Description                                                       | Data type | Required | Default value |
|-------------------|-------------------------------------------------------------------|-----------|----------|---------------|
| custom attributes | Any attributes that belong to the collection element to be added. | String    | No       |               |

 

**Child Elements**

None.

**Parent Elements**

| Parent Element                                                                | Description                                                                                            |
|-------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [**serverpreview:SectionData**](element-serverpreview-sectiondata-manual.md) | Identifies section data that will be embedded into applicationHost.config file of an IIS installation. |

 

## Examples


```XML
<Package ...
         xmlns:serverpreview=http://schemas.microsoft.com/appx/manifest/serverpreview/windows10"  
         IgnorableNamespaces="... serverpreview">
    <Applications>
        <Application>
            <Extensions>
                <serverpreview:Extension Category="windows.iisModules">  
                    <serverpreview:IisModules>  
                        <serverpreview:IisModule 
                                    Name="HypotheticalModule"  
                                    ModuleDll="hypothetical.dll"  
                                    SchemaFileName="hypothetical_schema.xml">  
                            <serverpreview:SectionData 
                                    SectionPath="hypothetical">  
                                <serverpreview:CollectionElement 
                                    Name="ruleNumber1"  
                                    Rule="someRule"/>  
                                <serverpreview:Attribute 
                                    Name="Attribute for hypothetical"  
                                    Value="value"/>  
                                <serverpreview:Attribute 
                                    Name="hostAffinityProviderListAttribute"                    
                                    Value="attributeValue"/>  
                            </serverpreview:SectionData>  
                        </serverpreview:IisModule>  
                    </serverpreview:IisModules> 
                </serverpreview:Extension>  
            </Extensions>
        </Application>
    </Applications>
</Package>
```

## Requirements


|               | Value                                                              |
|---------------|--------------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/serverpreview/windows10` |

 

 

 



