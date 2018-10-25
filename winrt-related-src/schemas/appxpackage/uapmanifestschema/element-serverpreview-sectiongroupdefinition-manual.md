---
Description: Identifies an Internet Information Service (IIS) SectionGroupDefinition as it pertains to a same-named XML element in an applicationHost.config file.
Search.Product: eADQiWindows 10XVcnh
title: serverpreview:SectionGroupDefinition
ms.assetid: 61a1d2f5-5742-414d-98ea-e9d43d831efc
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# serverpreview:SectionGroupDefinition


Identifies an Internet Information Service (IIS) SectionGroupDefinition as it pertains to a same-named XML element in an applicationHost.config file. The iisModule being installed claims ownership of this SectionGroupDefinition inside the applicationHost.config file of the IIS instance that is installed on the target machine. This behavior also means that if this SectionGroupDefinition already exists, installation is blocked.

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
<dd><b>&lt;serverpreview:SectionGroupDefinition&gt;</b></dd>
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
<serverpreview:SectionGroupDefinition Name = A string between 1 and 32767 
                                             characters in length with a 
                                             non-whitespace character at its 
                                             beginning and end.  >
  <!-- Child elements -->
    serverpreview:SectionGroupDefinition*
    serverpreview:SectionDefintion*
</serverpreview:SectionGroupDefintion>
```

**Key**

          \* optional (zero or more)

## Attributes and Elements


**Attributes**

| Attribute | Description                             | Data type                                                                                                   | Required | Default value |
|-----------|-----------------------------------------|-------------------------------------------------------------------------------------------------------------|----------|---------------|
| **Name**  | The name of the SectionGroupDefinition. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes      |               |

 

**Child Elements**

| Child Element                                                                             | Description                                                                                                                                                                                                                                    |
|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **serverpreview:SectionGroupDefinition**                                                  | Identifies an Internet Information Service (IIS) SectionGroupDefinition as it pertains to a same-named XML element in an applicationHost.config file. A SectionGroupDefinition may be nestled inside another if not defined at the root level. |
| [**serverpreview:SectionDefinition**](element-serverpreview-sectiondefinition-manual.md) | Identifies an Internet Information Service (IIS) SectionDefinition as it pertains to a same-named XML element in an applicationHost.config file.                                                                                               |

 

**Parent Elements**

| Parent Element                                                            | Description                                                                                                                                                                                                                                    |
|---------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**serverpreview:IisModule**](element-serverpreview-iismodule-manual.md) | Identifies an Internet Information Service (IIS) module to install, update, or uninstall out-of-band on Nano Server.                                                                                                                           |
| **serverpreview:SectionGroupDefinition**                                  | Identifies an Internet Information Service (IIS) SectionGroupDefinition as it pertains to a same-named XML element in an applicationHost.config file. A SectionGroupDefinition may be nestled inside another if not defined at the root level. |

 

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
                                    Name="RewriteModule"  
                                    ModuleDll="rewrite.dll"  
                                    SchemaFileName="rewrite_schema.xml">  
                            <serverpreview:SectionGroupDefinition 
                                    Name="rewrite">  
                                <serverpreview:SectionDefinition 
                                    Name="rules"  
                                    OverrideModeDefault="allow"/>  
                                <serverpreview:SectionDefinition 
                                    Name="globalRules"  
                                    OverrideModeDefault="deny"                    
                                    AllowDefinition="appHostOnly"/>  
                                <serverpreview:SectionDefinition 
                                    Name="outboundRules"  
                                    OverrideModeDefault="allow"/>  
                                <serverpreview:SectionDefinition 
                                    Name="providers"  
                                    OverrideModeDefault="allow"/>  
                                <serverpreview:SectionDefinition 
                                    Name="rewriteMaps"  
                                    OverrideModeDefault="allow"/>  
                                <serverpreview:SectionDefinition 
                                    Name="allowedServerVariables"                          
                                    OverrideModeDefault="deny"/>  
                            </serverpreview:SectionGroupDefinition>  
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

 

 

 



