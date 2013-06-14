//Maya ASCII 2011 scene
//Name: D:ambientLight1.ma
//Last modified: Thu, Jun 06, 2013 02:53:26 PM
//Codeset: 1252
requires maya "2011";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya batch mode";
fileInfo "version" "2011 Hotfix 3 x64";
fileInfo "cutIdentifier" "201007130320-777601";
fileInfo "osv" "Microsoft Windows 7 Ultimate Edition, 64-bit Windows 7  (Build 7600)\n";
createNode transform -n "ambientLight1";
createNode ambientLight -n "ambientLightShape1" -p "ambientLight1";
	setAttr -k off ".v";
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :renderPartition;
	setAttr -s 12 ".st";
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultShaderList1;
	setAttr -s 12 ".s";
select -ne :defaultTextureList1;
	setAttr -s 3 ".tx";
select -ne :lightList1;
	setAttr -s 3 ".l";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -s 3 ".u";
select -ne :renderGlobalsList1;
select -ne :initialMaterialInfo;
select -ne :defaultRenderGlobals;
	setAttr ".ren" -type "string" "vray";
select -ne :defaultLightSet;
	setAttr -s 3 ".dsm";
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
select -ne :defaultHardwareRenderGlobals;
	setAttr ".fn" -type "string" "im";
	setAttr ".res" -type "string" "ntsc_4d 646 485 1.333";
connectAttr "ambientLightShape1.ltd" ":lightList1.l" -na;
connectAttr "ambientLight1.iog" ":defaultLightSet.dsm" -na;
// End of D:ambientLight1.ma
