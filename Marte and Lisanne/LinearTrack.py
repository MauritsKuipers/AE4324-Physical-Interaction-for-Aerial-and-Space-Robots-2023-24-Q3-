from Transformation import transform_ee2ground
import matplotlib.pyplot as plt
import numpy as np
from ConstantVelocityTraj import constant_speed_trajectory


# track = {'time': [0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.060000000000000005, 0.06999999999999999, 0.08, 0.09, 0.09999999999999999, 0.11, 0.12, 0.13, 0.14, 0.15000000000000002, 0.16, 0.17, 0.18000000000000002, 0.19, 0.2, 0.21000000000000002, 0.22, 0.23, 0.24000000000000002, 0.25, 0.26, 0.27, 0.28, 0.29000000000000004, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35000000000000003, 0.36000000000000004, 0.37, 0.38, 0.39, 0.4, 0.41000000000000003, 0.42000000000000004, 0.43, 0.44, 0.45, 0.46, 0.47000000000000003, 0.48000000000000004, 0.49, 0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.5700000000000001, 0.5800000000000001, 0.59, 0.6, 0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.6900000000000001, 0.7000000000000001, 0.7100000000000001, 0.72, 0.73, 0.74, 0.75, 0.76, 0.77, 0.78, 0.79, 0.8, 0.81, 0.8200000000000001, 0.8300000000000001, 0.8400000000000001, 0.85, 0.86, 0.87, 0.88, 0.89, 0.9, 0.91, 0.92, 0.93, 0.9400000000000001, 0.9500000000000001, 0.9600000000000001, 0.97, 0.98, 0.99, 1.0, 1.01, 1.02, 1.03, 1.04, 1.05, 1.06, 1.07, 1.08, 1.09, 1.1, 1.11, 1.12, 1.1300000000000001, 1.1400000000000001, 1.1500000000000001, 1.1600000000000001, 1.17, 1.18, 1.19, 1.2, 1.21, 1.22, 1.23, 1.24, 1.25, 1.26, 1.27, 1.28, 1.29, 1.3, 1.31, 1.32, 1.33, 1.34, 1.35, 1.36, 1.37, 1.3800000000000001, 1.3900000000000001, 1.4000000000000001, 1.4100000000000001, 1.42, 1.43, 1.44, 1.45, 1.46, 1.47, 1.48, 1.49, 1.5, 1.51, 1.52, 1.53, 1.54, 1.55, 1.56, 1.57, 1.58, 1.59, 1.6, 1.61, 1.62, 1.6300000000000001, 1.6400000000000001, 1.6500000000000001, 1.6600000000000001, 1.6700000000000002, 1.68, 1.69, 1.7, 1.71, 1.72, 1.73, 1.74, 1.75, 1.76, 1.77, 1.78, 1.79, 1.8, 1.81, 1.82, 1.83, 1.84, 1.85, 1.86, 1.87, 1.8800000000000001, 1.8900000000000001, 1.9000000000000001, 1.9100000000000001, 1.9200000000000002, 1.93, 1.94, 1.95, 1.96, 1.97, 1.98, 1.99, 2.0, 2.01, 2.02, 2.03, 2.04, 2.05, 2.0599999999999996, 2.07, 2.0799999999999996, 2.09, 2.0999999999999996, 2.11, 2.1199999999999997, 2.13, 2.1399999999999997, 2.15, 2.1599999999999997, 2.17, 2.1799999999999997, 2.19, 2.1999999999999997, 2.21, 2.2199999999999998, 2.23, 2.2399999999999998, 2.25, 2.26, 2.27, 2.28, 2.29, 2.3, 2.31, 2.32, 2.3299999999999996, 2.34, 2.3499999999999996, 2.36, 2.3699999999999997, 2.38, 2.3899999999999997, 2.4, 2.4099999999999997, 2.42, 2.4299999999999997, 2.44, 2.4499999999999997, 2.46, 2.4699999999999998, 2.48, 2.4899999999999998, 2.5, 2.51, 2.52, 2.53, 2.54, 2.55, 2.56, 2.57, 2.5799999999999996, 2.59, 2.5999999999999996, 2.61, 2.6199999999999997, 2.63, 2.6399999999999997, 2.65, 2.6599999999999997, 2.67, 2.6799999999999997, 2.69, 2.6999999999999997, 2.71, 2.7199999999999998, 2.73, 2.7399999999999998, 2.75, 2.76, 2.77, 2.78, 2.79, 2.8, 2.81, 2.82, 2.8299999999999996, 2.84, 2.8499999999999996, 2.86, 2.8699999999999997, 2.88, 2.8899999999999997, 2.9, 2.9099999999999997, 2.92, 2.9299999999999997, 2.94, 2.9499999999999997, 2.96, 2.9699999999999998, 2.98, 2.9899999999999998], 
#          'theta_0': [0.17453292519943295, 0.17451156289474545, 0.17448104531662045, 0.17455428750412044, 0.17448104531662045, 0.17452987344162046, 0.17454818398849548, 0.1744749418009955, 0.17445052773849548, 0.17440169961349547, 0.17479232461349548, 0.1750852933634955, 0.1758665433634955, 0.175832974027558, 0.17583907754318298, 0.17579024941818297, 0.17576583535568296, 0.17576583535568296, 0.17579024941818297, 0.17576583535568296, 0.17576583535568296, 0.17579024941818297, 0.17580245644943296, 0.17579024941818297, 0.17576278359787048, 0.1757261625041205, 0.17570785195724548, 0.17568648965255798, 0.175588833402558, 0.175393520902558, 0.175381313871308, 0.17533858926193302, 0.175350796293183, 0.17546065957443302, 0.17544845254318303, 0.17543624551193304, 0.17543624551193304, 0.17541793496505803, 0.17539352090255803, 0.17519820840255804, 0.17517989785568303, 0.17520431191818303, 0.17519210488693304, 0.17519210488693304, 0.17509444863693305, 0.17509444863693305, 0.17509444863693305, 0.17514327676193306, 0.17513717324630806, 0.17518600137130808, 0.17515548379318308, 0.17510055215255807, 0.17505172402755806, 0.17507613809005806, 0.17505172402755806, 0.17502730996505805, 0.17497848184005804, 0.17507613809005804, 0.17505172402755803, 0.17514938027755803, 0.17518600137130802, 0.17523482949630803, 0.17496627480880803, 0.17495406777755804, 0.17497848184005804, 0.17498458535568304, 0.17497848184005804, 0.17502730996505805, 0.17522262246505804, 0.17514938027755805, 0.17517379434005806, 0.17516158730880807, 0.17517379434005806, 0.17517379434005806, 0.17510055215255807, 0.17512496621505808, 0.17510055215255807, 0.17508834512130808, 0.1751066556681831, 0.17514938027755808, 0.17514938027755808, 0.17512496621505808, 0.17478316934005808, 0.1747465482463081, 0.17472213418380808, 0.17472213418380808, 0.17473739297287058, 0.17297958047287057, 0.17296737344162058, 0.1729460111369331, 0.1729338041056831, 0.1729460111369331, 0.1728849759806831, 0.17283614785568308, 0.17332442910568308, 0.17336105019943307, 0.17335494668380808, 0.1733427396525581, 0.1733213773478706, 0.17333358437912058, 0.17330917031662058, 0.1733579984416206, 0.17334884316818308, 0.17335494668380808, 0.17341598184005808, 0.17339767129318306, 0.17342208535568307, 0.17337325723068306, 0.17327560098068306, 0.17320235879318308, 0.17320846230880807, 0.17319625527755808, 0.17316268594162057, 0.17315658242599558, 0.1730833402384956, 0.17308944375412058, 0.17296737344162058, 0.17290633828537058, 0.17291854531662057, 0.17292770059005808, 0.17295211465255808, 0.17304977090255808, 0.1730528226603706, 0.17296737344162058, 0.17295821816818308, 0.17297042519943306, 0.17295211465255805, 0.17295211465255805, 0.17296432168380804, 0.17297652871505803, 0.17297652871505803, 0.17298873574630802, 0.17297652871505803, 0.17295211465255803, 0.17290328652755801, 0.172884975980683, 0.17288650185958926, 0.17293532998458927, 0.17291091592208926, 0.17289260537521425, 0.17289870889083925, 0.17288955361740174, 0.172884975980683, 0.1728819242228705, 0.17289413125412048, 0.17286971719162048, 0.17287582070724547, 0.17287429482833921, 0.1728712430705267, 0.1728559842814642, 0.1728468290080267, 0.1728407254924017, 0.17283843667404233, 0.17285674722091735, 0.17285674722091735, 0.1728521695841986, 0.1728338590373236, 0.17282241494552672, 0.1730177274455267, 0.17303603799240172, 0.17305129678146422, 0.17302993447677673, 0.17303298623458924, 0.17302077920333925, 0.17302993447677675, 0.17346938760177674, 0.17337173135177675, 0.17334731728927674, 0.17335952432052673, 0.17335342080490174, 0.17335342080490174, 0.17333511025802673, 0.17331985146896423, 0.17314895303146421, 0.1722700467814642, 0.1722456327189642, 0.1722120633830267, 0.17220138223068293, 0.17337325723068292, 0.17337325723068292, 0.17334426553146418, 0.17332595498458916, 0.17332595498458916, 0.17329238564865165, 0.17329848916427665, 0.17330125481979422, 0.1733004918803411, 0.17330402047531182, 0.17330535561935478, 0.1732321134318548, 0.17322906167404228, 0.17321303994552667, 0.17321513802902277, 0.17318996102706966, 0.17319263131515558, 0.17319129617111262, 0.17319339425460872, 0.1732078901042181, 0.17320960671798763, 0.1732149472941595, 0.17321723611251888, 0.17322181374923762, 0.1732191434611517, 0.1732191434611517, 0.1732170453776556, 0.1732189527262884, 0.17322162301437433, 0.1732178083171087, 0.17321857125656182, 0.17322009713546807, 0.17322848946945243, 0.17322696359054618, 0.17308047921554617, 0.17308257729904228, 0.17307990701095635, 0.17307990701095635, 0.1730732312907415, 0.17307780892746025, 0.1730793348063665, 0.1730793348063665, 0.17308925301925712, 0.17308314950363213, 0.17309230477706963, 0.1730572095622259, 0.17305415780441338, 0.1730572095622259, 0.17302364022628838, 0.17302058846847587, 0.17302974374191338, 0.1730327954997259, 0.17303050668136652, 0.17302440316574152, 0.17302440316574152, 0.17299693734542904, 0.17303355843917903, 0.17303203256027277, 0.17303813607589777, 0.17303203256027277, 0.17302592904464778, 0.17303355843917903, 0.17301524789230402, 0.17302287728683527, 0.17302592904464778, 0.17303203256027277, 0.17303355843917903, 0.17301524789230402, 0.17301524789230402, 0.17301829965011653, 0.17301829965011653, 0.17303661019699154, 0.17303661019699154, 0.17303966195480405, 0.17302745492355406, 0.17305186898605407, 0.17373546273605406, 0.17371104867355405, 0.17372020394699156, 0.17372020394699156, 0.17375072152511656, 0.17376292855636655, 0.17383617074386654, 0.17384532601730404, 0.17379649789230403, 0.17379649789230403, 0.17379649789230403, 0.17374766976730402, 0.173662220548554, 0.17366527230636652, 0.1737079969157415, 0.1737202039469915, 0.1737690320719915, 0.1738056531657415, 0.1737079969157415, 0.17372630746261652, 0.17372630746261652, 0.17370189340011652, 0.17373241097824152, 0.17373241097824152, 0.17314647347824152, 0.17314036996261653, 0.17316173226730402, 0.17313731820480402, 0.173173939298554, 0.17313731820480402, 0.173149525236054, 0.17344249398605402, 0.17344249398605402, 0.17336925179855403, 0.17335094125167902, 0.1733478894938665, 0.1723713269938665, 0.1723652234782415, 0.17226756722824152, 0.1734394422282415, 0.1734150281657415, 0.1736103406657415, 0.1736103406657415, 0.1736103406657415, 0.1743915906657415, 0.1744892469157415], 
#          'theta_1': [0.2617993877991494, 0.2611157940491494, 0.2603345440491494, 0.26189704404914943, 0.2611157940491494, 0.26267829404914944, 0.26287360654914943, 0.2620923565491494, 0.2613111065491494, 0.2601392315491494, 0.27263923154914943, 0.27732673154914944, 0.2992017315491494, 0.29832282529914944, 0.29832282529914944, 0.29715095029914945, 0.2967603252991495, 0.29617438779914945, 0.2967603252991495, 0.2965650127991495, 0.2963697002991495, 0.2979322002991495, 0.29773688779914953, 0.2974439190491495, 0.2969556377991495, 0.2959790752991495, 0.2953931377991495, 0.2949048565491495, 0.2949048565491495, 0.2886548565491495, 0.2886548565491495, 0.2876782940491495, 0.2876782940491495, 0.2900220440491495, 0.2902173565491495, 0.29060798154914946, 0.29099860654914944, 0.29060798154914946, 0.2904126690491495, 0.2872876690491495, 0.2866040752991495, 0.2866040752991495, 0.2863111065491495, 0.2831861065491495, 0.2847486065491495, 0.2839673565491495, 0.2827954815491495, 0.2827954815491495, 0.2829907940491495, 0.2837720440491495, 0.2829907940491495, 0.28162360654914953, 0.27927985654914955, 0.27967048154914953, 0.27771735654914953, 0.27927985654914955, 0.28006110654914956, 0.2847486065491496, 0.2847486065491496, 0.28709235654914955, 0.28826423154914954, 0.28904548154914955, 0.2827954815491496, 0.2824048565491496, 0.2831861065491496, 0.2833814190491496, 0.2831861065491496, 0.2835767315491496, 0.2867017315491496, 0.28513923154914955, 0.28513923154914955, 0.28513923154914955, 0.28533454404914954, 0.28494391904914956, 0.28299079404914956, 0.28494391904914956, 0.2845532940491496, 0.2845532940491496, 0.2851392315491496, 0.28572516904914963, 0.28552985654914964, 0.28513923154914966, 0.28045173154914965, 0.27771735654914964, 0.27693610654914963, 0.27654548154914965, 0.27674079404914964, 0.21424079404914964, 0.21365485654914965, 0.21297126279914966, 0.21258063779914965, 0.21238532529914966, 0.21004157529914966, 0.20808845029914966, 0.21746345029914965, 0.21785407529914966, 0.21863532529914967, 0.21804938779914967, 0.21765876279914967, 0.21844001279914968, 0.21687751279914969, 0.22000251279914967, 0.21951423154914967, 0.22068610654914966, 0.22420173154914966, 0.22322516904914966, 0.22381110654914965, 0.22263923154914966, 0.22029548154914966, 0.21717048154914967, 0.21707282529914967, 0.21746345029914968, 0.21648688779914968, 0.21609626279914967, 0.21297126279914969, 0.21316657529914967, 0.20613532529914969, 0.20340095029914967, 0.20183845029914968, 0.20222907529914969, 0.20535407529914967, 0.21160407529914968, 0.21219001279914967, 0.21297126279914969, 0.2123853252991497, 0.21258063779914968, 0.2114087627991497, 0.2114087627991497, 0.2114087627991497, 0.2082837627991497, 0.2076978252991497, 0.20847907529914972, 0.20730720029914973, 0.20554938779914972, 0.20437751279914973, 0.20340095029914973, 0.20359626279914972, 0.2067212627991497, 0.2051587627991497, 0.20359626279914972, 0.2028150127991497, 0.2014478252991497, 0.2017407940491497, 0.2013501690491497, 0.2029126690491497, 0.2029126690491497, 0.2036939190491497, 0.20349860654914972, 0.20305915342414974, 0.20130134092414972, 0.20071540342414973, 0.19973884092414973, 0.19993415342414972, 0.1975904034241497, 0.19446540342414972, 0.19397712217414972, 0.19436774717414973, 0.19339118467414973, 0.22464118467414973, 0.22464118467414973, 0.22503180967414974, 0.22385993467414975, 0.22346930967414974, 0.22298102842414974, 0.22317634092414973, 0.23255134092414972, 0.2356763409241497, 0.23411384092414972, 0.23411384092414972, 0.23411384092414972, 0.23450446592414972, 0.23391852842414973, 0.23264899717414972, 0.2263989971741497, 0.1951489971741497, 0.19397712217414972, 0.19202399717414972, 0.19134040342414974, 0.27884040342414973, 0.27766852842414974, 0.27630134092414976, 0.27552009092414975, 0.25052009092414973, 0.2606763409241497, 0.2636060284241497, 0.2628247784241497, 0.2600904034241497, 0.2598462627991497, 0.2596021221741497, 0.2674146221741497, 0.2688794659241497, 0.27219977842414966, 0.27146735654914966, 0.27927985654914966, 0.27576423154914964, 0.27683845029914966, 0.2766431377991497, 0.26531501279914965, 0.26472907529914963, 0.26648688779914964, 0.26573005186164966, 0.2665113018616497, 0.2668042706116497, 0.2670484112366497, 0.2678296612366497, 0.2679273174866497, 0.2673902081116497, 0.2671948956116497, 0.2671460674866497, 0.2671460674866497, 0.2653882549866497, 0.2673413799866497, 0.2767163799866497, 0.27583747373664974, 0.27710700498664975, 0.27700934873664973, 0.27974372373664974, 0.2781812237366497, 0.27700934873664973, 0.27896247373664973, 0.27710700498664975, 0.27398200498664976, 0.2726148174866498, 0.27495856748664976, 0.27515387998664975, 0.27481208311164973, 0.27871833311164973, 0.2788648174866497, 0.27847419248664973, 0.28003669248664975, 0.2801343487366498, 0.2802320049866498, 0.2797437237366498, 0.2820874737366498, 0.2789624737366498, 0.27837653623664976, 0.2781812237366498, 0.27857184873664975, 0.27837653623664976, 0.27837653623664976, 0.2772046612366498, 0.27691169248664976, 0.27642341123664976, 0.2762280987366498, 0.27613044248664975, 0.27691169248664976, 0.2581616924866498, 0.2579663799866498, 0.2569898174866498, 0.25738044248664976, 0.28863044248664976, 0.28833747373664975, 0.29029059873664975, 0.28931403623664975, 0.27993903623664973, 0.28052497373664975, 0.28072028623664974, 0.27993903623664973, 0.27954841123664975, 0.27993903623664973, 0.27681403623664974, 0.2762280987366497, 0.27700934873664973, 0.2762280987366497, 0.2762280987366497, 0.27310309873664973, 0.27388434873664974, 0.27349372373664976, 0.27349372373664976, 0.27349372373664976, 0.27271247373664975, 0.27075934873664975, 0.27700934873664973, 0.27661872373664975, 0.2772046612366498, 0.2787671612366498, 0.2779859112366498, 0.2756421612366498, 0.2943921612366498, 0.2947827862366498, 0.29419684873664975, 0.29732184873664974, 0.29595466123664976, 0.29790778623664976, 0.29712653623664975, 0.28462653623664974, 0.28462653623664974, 0.2869702862366497, 0.2861890362366497, 0.2859937237366497, 0.2734937237366497, 0.2732984112366497, 0.27407966123664973, 0.2615796612366497, 0.2607984112366497, 0.2514234112366497, 0.2506421612366497, 0.2514234112366497, 0.24517341123664968, 0.2420484112366497], 
#          'theta_2': [2.356194490192345, 2.356194490192345, 2.3563898026923447, 2.3579523026923446, 2.3567804276923447, 2.356585115192345, 2.356389802692345, 2.356780427692345, 2.356975740192345, 2.356585115192345, 2.353460115192345, 2.356585115192345, 2.358147615192345, 2.358147615192345, 2.358538240192345, 2.359319490192345, 2.359319490192345, 2.359319490192345, 2.359807771442345, 2.360003083942345, 2.359905427692345, 2.360491365192345, 2.3606866776923447, 2.360735505817345, 2.360784333942345, 2.360881990192345, 2.361077302692345, 2.3611749589423447, 2.3611749589423447, 2.3642999589423446, 2.3641046464423447, 2.3641046464423447, 2.3642999589423446, 2.3648858964423445, 2.3646905839423447, 2.3651788651923447, 2.3653741776923445, 2.3652765214423446, 2.3652765214423446, 2.3652765214423446, 2.3651788651923447, 2.365960115192345, 2.3660577714423447, 2.3676202714423447, 2.3676202714423447, 2.3678155839423445, 2.3674249589423444, 2.3682062089423446, 2.3685968339423447, 2.3689874589423447, 2.368792146442345, 2.3684991776923447, 2.3677179276923446, 2.3680108964423447, 2.3676202714423447, 2.3668390214423445, 2.3676202714423447, 2.368401521442345, 2.3695733964423447, 2.3699640214423447, 2.370745271442345, 2.370354646442345, 2.371135896442345, 2.370940583942345, 2.372112458942345, 2.372503083942345, 2.372503083942345, 2.372893708942345, 2.372893708942345, 2.3732843339423453, 2.3721124589423455, 2.3730890214423455, 2.3732843339423453, 2.3731866776923454, 2.3726007401923455, 2.3724054276923456, 2.3727960526923457, 2.373186677692346, 2.3738702714423456, 2.3741144120673456, 2.3740655839423455, 2.3739679276923455, 2.3770929276923454, 2.3770929276923454, 2.3771905839423453, 2.3776788651923453, 2.3779230058173453, 2.3669855058173455, 2.3671808183173453, 2.3671808183173453, 2.366790193317345, 2.366790193317345, 2.367376130817345, 2.367766755817345, 2.369329255817345, 2.369329255817345, 2.368938630817345, 2.369329255817345, 2.369426912067345, 2.369231599567345, 2.3686456620673453, 2.367864412067345, 2.367620271442345, 2.367815583942345, 2.367815583942345, 2.367327302692345, 2.367424958942345, 2.366741365192345, 2.366741365192345, 2.366546052692345, 2.366643708942345, 2.3654718339423453, 2.3654718339423453, 2.365813630817345, 2.365813630817345, 2.365520662067345, 2.366692537067345, 2.3663019120673447, 2.3668878495673447, 2.366692537067345, 2.3639581620673447, 2.3670831620673445, 2.3668878495673447, 2.3688409745673447, 2.3688653886298447, 2.3687189042548447, 2.3691095292548447, 2.3706720292548447, 2.3722345292548446, 2.3728204667548445, 2.3735040605048443, 2.3737482011298443, 2.373357576129844, 2.373357576129844, 2.373357576129844, 2.373113435504844, 2.3731622636298444, 2.3758966386298446, 2.3753107011298447, 2.3757013261298447, 2.3762872636298447, 2.3760431230048447, 2.3759454667548447, 2.3760431230048447, 2.3766290605048446, 2.3766290605048446, 2.3781915605048445, 2.3784601151923446, 2.3785333573798444, 2.378240388629844, 2.378313630817344, 2.378264802692344, 2.3780939042548437, 2.3796564042548436, 2.3796564042548436, 2.3795343339423436, 2.3799249589423437, 2.3799005448798436, 2.3736505448798435, 2.3730646073798436, 2.3732599198798434, 2.3730646073798436, 2.3731622636298435, 2.3731866776923436, 2.3731378495673434, 2.3731378495673434, 2.3715753495673435, 2.3711847245673434, 2.3723565995673432, 2.3724054276923434, 2.3724054276923434, 2.3725519120673435, 2.3726739823798435, 2.3742364823798434, 2.3711114823798436, 2.3711114823798436, 2.3714044511298438, 2.3712579667548437, 2.3962579667548436, 2.3961114823798435, 2.3961114823798435, 2.3962579667548436, 2.4025079667548437, 2.4021661698798438, 2.4022638261298437, 2.402230256793906, 2.402157014606406, 2.4021707475165623, 2.40208224654, 2.40188693404, 2.401685518024375, 2.401441377399375, 2.4014688432196873, 2.4013223588446873, 2.401273530719687, 2.4011972367743746, 2.4009897172431245, 2.4018686234931246, 2.4018686234931246, 2.4016733109931248, 2.401697725055625, 2.401502412555625, 2.4014718949775, 2.40150851607125, 2.40138644575875, 2.40123996138375, 2.4012216508368747, 2.4013071000556248, 2.4012796342353124, 2.4013223588446873, 2.401420015094687, 2.401127046344687, 2.401517671344687, 2.401407808063437, 2.401407808063437, 2.4013894975165617, 2.4012430131415616, 2.4010599076728116, 2.401047700641562, 2.401072114704062, 2.401072114704062, 2.398533052204062, 2.398679536579062, 2.398313325641562, 2.3983621537665623, 2.3982889115790624, 2.3980935990790626, 2.3979715287665626, 2.397715181110313, 2.3973245561103127, 2.397312349079063, 2.3973855912665627, 2.397287935016563, 2.397043794391563, 2.3976297318915627, 2.3974832475165626, 2.397287935016563, 2.3972391068915626, 2.3969461381415624, 2.3967264115790625, 2.3966287553290626, 2.396555513141563, 2.3965310990790627, 2.3963846147040626, 2.396189302204063, 2.395505708454063, 2.383005708454063, 2.382810395954063, 2.382859224079063, 2.382810395954063, 2.370310395954063, 2.370115083454063, 2.369431489704063, 2.3693338334540632, 2.3677713334540633, 2.367478364704063, 2.367087739704063, 2.367087739704063, 2.367087739704063, 2.367087739704063, 2.366306489704063, 2.366208833454063, 2.366404145954063, 2.366404145954063, 2.3660135209540627, 2.3675760209540626, 2.3677713334540624, 2.3678689897040623, 2.3678689897040623, 2.367576020954062, 2.3679666459540623, 2.3684549272040623, 2.370017427204062, 2.370017427204062, 2.369626802204062, 2.368064302204062, 2.368064302204062, 2.367283052204062, 2.361033052204062, 2.3612283647040617, 2.361130708454062, 2.3603494584540616, 2.3607400834540617, 2.3597635209540617, 2.3599588334540615, 2.3646463334540617, 2.365427583454062, 2.365036958454062, 2.3647439897040616, 2.3647439897040616, 2.3678689897040615, 2.3677713334540615, 2.3665994584540617, 2.372849458454062, 2.373240083454062, 2.373240083454062, 2.373044770954062, 2.372654145954062, 2.385154145954062, 2.382810395954062], 
#          'theta_3': [-0.8377580409572782, -0.8389299159572783, -0.8385392909572783, -0.8416642909572783, -0.8385392909572783, -0.8393205409572783, -0.8393205409572783, -0.8416642909572782, -0.8416642909572782, -0.8385392909572782, -0.8385392909572782, -0.8572892909572782, -0.8697892909572782, -0.8701799159572782, -0.8725236659572781, -0.8756486659572782, -0.8764299159572781, -0.8779924159572782, -0.8795549159572782, -0.8807267909572782, -0.8822892909572783, -0.8854142909572783, -0.8873674159572783, -0.8877580409572783, -0.8881486659572783, -0.8889299159572782, -0.8904924159572782, -0.8914689784572782, -0.8664689784572782, -0.8602189784572782, -0.8613908534572783, -0.8617814784572783, -0.8610002284572783, -0.8656877284572783, -0.8656877284572783, -0.8680314784572782, -0.8688127284572782, -0.8699846034572782, -0.8699846034572782, -0.8684221034572782, -0.8695939784572783, -0.8742814784572782, -0.8746721034572782, -0.8809221034572782, -0.8809221034572782, -0.8824846034572782, -0.8801408534572782, -0.8801408534572782, -0.8824846034572782, -0.8863908534572782, -0.8863908534572782, -0.8867814784572782, -0.8820939784572782, -0.8828752284572782, -0.8828752284572782, -0.8828752284572782, -0.8828752284572782, -0.8828752284572782, -0.8844377284572782, -0.8891252284572781, -0.8930314784572781, -0.8992814784572781, -0.8930314784572781, -0.8930314784572781, -0.8930314784572781, -0.8930314784572781, -0.8942033534572782, -0.8981096034572782, -0.9043596034572782, -0.9043596034572782, -0.9027971034572781, -0.9059221034572782, -0.9063127284572782, -0.9063127284572782, -0.9039689784572782, -0.9086564784572781, -0.9110002284572781, -0.9110002284572781, -0.9133439784572781, -0.9156877284572781, -0.9160783534572781, -0.9172502284572781, -0.9235002284572781, -0.924281478457278, -0.925062728457278, -0.928187728457278, -0.9293596034572781, -0.816859603457278, -0.817640853457278, -0.818422103457278, -0.8188127284572779, -0.8188127284572779, -0.820375228457278, -0.820375228457278, -0.8328752284572779, -0.8336564784572779, -0.8344377284572778, -0.8367814784572778, -0.8375627284572777, -0.8360002284572777, -0.8344377284572777, -0.8313127284572777, -0.8309221034572777, -0.8324846034572777, -0.8371721034572777, -0.8363908534572777, -0.8379533534572777, -0.8363908534572777, -0.8363908534572777, -0.8332658534572777, -0.8340471034572776, -0.8356096034572776, -0.8356096034572776, -0.8379533534572776, -0.8379533534572776, -0.8363908534572776, -0.8332658534572775, -0.8317033534572775, -0.8332658534572775, -0.8336564784572775, -0.8336564784572775, -0.8461564784572775, -0.8465471034572775, -0.8559221034572775, -0.8567033534572774, -0.8563127284572775, -0.8594377284572775, -0.8625627284572775, -0.8688127284572775, -0.8688127284572775, -0.8715471034572775, -0.8719377284572775, -0.8688127284572774, -0.8680314784572775, -0.8680314784572775, -0.8672502284572775, -0.8684221034572775, -0.8715471034572776, -0.8777971034572776, -0.8793596034572776, -0.8824846034572776, -0.8824846034572776, -0.8832658534572776, -0.8836564784572776, -0.8899064784572775, -0.8930314784572776, -0.8961564784572776, -0.8973283534572777, -0.8981096034572776, -0.8965471034572776, -0.8973283534572776, -0.8973283534572776, -0.8971330409572775, -0.9018205409572775, -0.8893205409572775, -0.8869767909572775, -0.8901017909572776, -0.8897111659572776, -0.9022111659572776, -0.8975236659572776, -0.8983049159572776, -0.8967424159572775, -0.8975236659572775, -0.8985002284572775, -0.8992814784572775, -0.8992814784572775, -0.8867814784572775, -0.8860002284572775, -0.8922502284572775, -0.8934221034572776, -0.8942033534572775, -0.8949846034572775, -0.8957658534572774, -0.9020158534572774, -0.8395158534572774, -0.8387346034572775, -0.8395158534572774, -0.8395158534572774, -0.9895158534572774, -0.9887346034572775, -0.9891252284572775, -0.9899064784572774, -1.1149064784572773, -1.1172502284572774, -1.1242814784572774, -1.1274064784572775, -1.1324846034572775, -1.1330217128322775, -1.1349748378322775, -1.1443498378322774, -1.1461076503322774, -1.1484514003322774, -1.1494279628322774, -1.1494279628322774, -1.1474748378322774, -1.1495256190822774, -1.1542131190822773, -1.1385881190822773, -1.1387834315822774, -1.1446428065822774, -1.1446916347072773, -1.1466447597072773, -1.1486955409572772, -1.1500627284572773, -1.1512346034572774, -1.1529924159572773, -1.1541642909572774, -1.1547502284572773, -1.1556291347072774, -1.1567033534572773, -1.1578752284572773, -1.1590471034572774, -1.1527971034572773, -1.1524064784572772, -1.1547502284572773, -1.1551896815822773, -1.1585099940822774, -1.1635881190822774, -1.1645646815822774, -1.1676896815822775, -1.1672990565822774, -1.1797990565822774, -1.1801896815822774, -1.1840959315822774, -1.1848771815822774, -1.1857560878322775, -1.1896623378322775, -1.1914201503322774, -1.1931779628322774, -1.1978654628322774, -1.1993303065822774, -1.2012834315822774, -1.2022599940822774, -1.2053849940822774, -1.2038224940822775, -1.2049943690822775, -1.2053849940822776, -1.2063615565822776, -1.2083146815822776, -1.2087053065822777, -1.2063615565822776, -1.2073381190822776, -1.2071428065822776, -1.2071428065822776, -1.2085099940822777, -1.2061662440822776, -1.2186662440822775, -1.2192521815822774, -1.2196428065822775, -1.2208146815822776, -1.2333146815822775, -1.2344865565822776, -1.2376115565822776, -1.2372209315822775, -1.2309709315822774, -1.2309709315822774, -1.2329240565822774, -1.2329240565822774, -1.2337053065822774, -1.2364396815822774, -1.2364396815822774, -1.2368303065822774, -1.2368303065822774, -1.2380021815822775, -1.2380021815822775, -1.2380021815822775, -1.2387834315822774, -1.2393693690822774, -1.2393693690822774, -1.2405412440822774, -1.2421037440822773, -1.2428849940822773, -1.2491349940822774, -1.2499162440822773, -1.2514787440822772, -1.2546037440822773, -1.2549943690822774, -1.2557756190822773, -1.2682756190822773, -1.2686662440822774, -1.2692521815822773, -1.2715959315822774, -1.2715959315822774, -1.2723771815822773, -1.2731584315822773, -1.2794084315822774, -1.2762834315822773, -1.2762834315822773, -1.2762834315822773, -1.2764787440822774, -1.3014787440822773, -1.3024553065822773, -1.3047990565822774, -1.2985490565822773, -1.2977678065822773, -1.2962053065822774, -1.2965959315822775, -1.2965959315822775, -1.2715959315822776, -1.2715959315822776]
#          }

pos = {
    "t": [],
    "x": [],
    "y": [],
    "z": []
}

initial_state =     {
        "theta_0": np.deg2rad(10),
        "theta_1": np.deg2rad(15),
        "theta_2": np.deg2rad(135),
        "theta_3": np.deg2rad(-48)
    }

velocity = np.array([[30], [0], [0]])

track = constant_speed_trajectory(velocity, initial_state)

for t in track["time"]:
    ind = track["time"].index(t)
    trans_mat = transform_ee2ground(track['theta_0'][ind], track['theta_1'][ind], track['theta_2'][ind], track['theta_3'][ind])

    x = trans_mat[0,3]
    y = trans_mat[1,3]
    z = trans_mat[2,3]

    pos["t"].append(t)
    pos['x'].append(x)
    pos['y'].append(y)
    pos['z'].append(z)



fig, axs = plt.subplots(4, sharex=True, sharey=False)
axs[0].plot(pos['t'], pos['x'])
axs[0].set_ylabel("x [mm]")
axs[0].grid()

axs[1].plot(pos['t'], pos['y'])
axs[1].set_ylabel("y [mm]")
axs[1].grid()

axs[2].plot(pos['t'], pos['z'])
axs[2].set_ylabel("z [mm]")
axs[2].grid()

axs[3].plot(track['time'], np.rad2deg(track['theta_0']), label='t0')
axs[3].plot(track['time'], np.rad2deg(track['theta_1']), label='t1')
axs[3].plot(track['time'], np.rad2deg(track['theta_2']), label='t2')
axs[3].plot(track['time'], np.rad2deg(track['theta_3']), label='t3')
axs[3].set_ylabel("angles [deg]")
axs[3].grid()
plt.legend()
plt.show()