---
Description: Identifies section data that will be embedded into applicationHost.config file of an IIS installation.
Search.Product: eADQiWindows 10XVcnh
title: serverpreview:SectionData
ms.assetid: 1182ba2d-ad98-4584-ba9b-935ee18aa5f4
author: mcleanbyron
ms.author: mcleans
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# serverpreview:SectionData


Identifies section data that will be embedded into applicationHost.config file of an IIS installation. Each **SectionData** element specifies one combination of a section and a path as determined by the attributes of the element. Modules can write section data anywhere in the configuration and these modules do not need ownership of these sections through a corresponding [**SectionDefinition**](element-serverpreview-sectiondefinition-manual.md) element. If the module does not own the section, the corresponding section needs to be defined already in the applicationHost.config file with the corresponding **SectionDefinition** element.

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
<dd><b>&lt;serverpreview:SectionData&gt;</b></dd>
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

[**&lt;Package&gt;**](element-package.md)

          [**&lt;Applications&gt;**](element-applications.md)

                    [**&lt;Application&gt;**](element-application.md)

                              [**&lt;Extensions&gt;**](element-1-extensions.md)

                                        [**&lt;serverpreview:Extension&gt;**](element-serverpreview-extension-manual.md)

                                                  [**&lt;serverpreview:IisModules&gt;**](element-serverpreview-iismodules-manual.md)

                                                            [**&lt;serverpreview:IisModule&gt;**](element-serverpreview-iismodule-manual.md)

                                                                      **&lt;serverpreview:SectionData&gt;**

## Syntax


```
<serverpreview:SectionData SectionPath = A string between 1 and 32767 characters 
                                         in length with a non-whitespace 
                                         character at its beginning and end. 
                           SubPath     = A string between 1 and 32767 characters 
                                         in length with a non-whitespace character 
                                         at its beginning and end. >
  <!-- Child elements -->
    ( serverpreview:CollectionElement |
      serverpreview:Attribute )*
</serverpreview:SectionData>
```

**Key**

          \* optional (zero or more)

## Attributes and Elements


**Attributes**

| Attribute       | Description                                                                                                                          | Data type                                                                                                   | Required | Default value |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|----------|---------------|
| **SectionPath** | The full path to the section into which the data should be embedded.                                                                 | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes      |               |
| **SubPath**     | An optional subpath structure for each subpath element, in which the parts of the structure are separated by the slash (/) character | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No       |               |

 

**Child Elements**

| Child Element                                                                             | Description                                                                                                            |
|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [**serverpreview:CollectionElement**](element-serverpreview-collectionelement-manual.md) | Represents a collection element with the specified attributes that should be added to the applicationHost.config file. |
| [**serverpreview:Attribute**](element-serverpreview-attribute-manual.md)                 | Represents an attiribute that should be added to or modified in the applicationHost.config file.                       |

 

**Parent Elements**

| Parent Element                                                            | Description                                                                                                          |
|---------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [**serverpreview:IisModule**](element-serverpreview-iismodule-manual.md) | Identifies an Internet Information Service (IIS) module to install, update, or uninstall out-of-band on Nano Server. |

 

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


|               |                                                                    |
|---------------|--------------------------------------------------------------------|
| **Namespace** | http://schemas.microsoft.com/appx/manifest/serverpreview/windows10 |

 

 

 



