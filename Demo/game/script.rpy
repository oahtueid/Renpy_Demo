# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Chi")
define sup = Character()
define uk = Character("???")
define t = Character("Trực", image="truc.png")
define h = Character("Hồng", image="hong.png")
define narrator = nvl_narrator

image black = "#000"
image phone : 
    "phone.png"
    zoom 2.0

image street:
    "street.jpg"
    zoom 3.5

image courtyard:
    "courtyard.jpg"
    zoom 3.5

image canteen:
    "canteen.jpg"
    zoom 2.0

image classroom:
    "classroom.webp"
    zoom 3.25
# The game starts here.

label start:


    scene black
    

    # These display lines of dialogue.

    play sound "beep.mp3" volume 1.0
    queue sound "beep.mp3" volume 1.0
    queue sound "beep.mp3" volume 1.0

    "{i}RING, RING, RING{/i}"

    nvl clear

    sup '"Ugh..."'

    "Có gì đó đang reo."

    play sound "beep.mp3" volume 1.0
    queue sound "beep.mp3" volume 1.0
    queue sound "beep.mp3" volume 1.0

    "{i}RING, RING, RING{/i}"

    "Ồn ào thật."

    "Tôi cố gắng với lấy chiếc điện thoại bằng một tay, còn dùng tay kia để dụi mắt."

    nvl clear

    "Trong căn phòng trọ tối om, tiếng chuông liên tục vang lên mặc kệ sự khó chịu của chủ nhân nó."

    "Tôi dụi mắt, đẩy tóc xõa hết về một bên, nhìn cho rõ màn hình điện thoại."

    show phone at right

    "Tôi cứ nghĩ đây chỉ là tiếng chuông báo thức mà thôi, nhưng có vẻ tôi đã nhầm."

    'Trên chiếc điện thoại hiện rõ dòng chữ: "A Mẹ Yêu"'

    "Mẹ tôi gọi ư? Có chuyện gì mà mẹ tôi lại gọi sớm thế nhỉ?"

    "Không chần chừ, tôi nhấn trả lời."

    nvl clear

    sup '"Alo, mẹ à?" {w}{i}*Ho*{/i}{w=0.5} Con đây, mẹ gọi con có việc gì không ạ?"'
    
    "Cố gắng nói chuyện ngay sau khi thức dậy làm cổ họng tôi nóng nảy và cọc cằn hẳn."

    nvl clear
    
    sup '"Chi à? Dậy chưa con?"'
    
    m '{i}*Ngáp*{/i}{w=0.5} "Dạ con mới dậy."'
    
    'Tôi trả lời mẹ tôi bằng một giọng uể oải.'

    nvl clear

    sup '"Mới dậy? 7h rồi mà mới dậy? Nay không đi học hả con?"'
    
    m '"Con học lúc 7h45 ạ..."'
    
    '7h45... Nếu tôi nhớ không nhầm thì tôi đã để chuông lúc 6h30 để có thể dậy làm đồ ăn sáng.'
    
    '6h30... Và giờ là 7h...'

    'Ôi không.'

    nvl clear

    play sound "<from 0.2>slap.mp3" volume 2.0

    m '"Ahhh... Con bị trễ rồi!"' with hpunch

    'Như có nước lạnh đổ lên đầu, tôi ngồi phắt dậy, bỏ chăn ra, lấy tay sờ về phía tường tìm kiếm cái công tắc đèn.'
    
    nvl clear

    sup '"..."'
    
    'Tôi có thể cảm nhận mẹ tôi đang thở dài dù điện thoại chỉ phản hồi với sự im lặng.'

    nvl clear

    'Biết nói gì đây.'

    'Tối qua tôi mải lo làm cái bức tranh mới quá nên ngủ muộn.'

    'Dạo gần đây tôi phải lo làm đồ án, làm thêm, rồi còn phải lo việc nhà như giặt đồ, nấu cơm, chỉ có tối qua thì tôi mới rảnh ra chút.'

    'Lo tập trung vẽ quá, đồng hồ chỉ 3h sáng lúc nào tôi không để ý.'

    nvl clear

    sup '"Giờ sống một mình thì phải tự lập lên chứ con. Cái gì cũng phải để nhắc thì khi nào mới trưởng thành được. *Tch*. Mà tối qua làm cái gì mà lại ngủ muộn hả?"'
    
    m '"... Dạ, con… Uhm, con học bài ạ."'

    sup '"Thiệt không đó?"'

    m '"Dạ thiệt."'

    'Tôi không thích việc nói dối với mẹ tôi, nhưng có những lúc làm vậy là cần thiết.'

    'Ví dụ như bây giờ.'

    nvl clear

    sup '"..."'

    'Mẹ tôi không nói gì, nhưng tôi có thể cảm nhận sự nghi ngờ hiển hiện rõ trên nét mặt mẹ tôi.'

    'Đôi mắt nhíp lại và bờ môi nhếch về bên trái, như khi mẹ tôi phải đãi gạo, sàng qua sàng lại cái thúng cho đến khi moi ra tất cả hạt sạn, hạt cát, hạt hỏng thì mới thôi.'

    'Đây không phải lần đầu tôi nói dối, cái nỗi khổ của tôi thì chỉ có mình tôi hiểu, dù tôi có kể, mẹ tôi cũng khó mà chấp nhận được, có khi hai người lại còn cãi nhau.'

    'Nhưng vì không phải lần đầu nên tôi đã quá quen với cái chiến thuật cần thiết để thoát khỏi cái tình huống khó xử này.'

    nvl clear

    m '"Mẹ ơi, mẹ gọi con có việc gì không ạ?"'

    sup '"...Không. Mẹ thích thì mẹ gọi thôi. Phải có việc gì thì mẹ mới được gọi à?"'

    m '"Dạ không... Nhưng nếu không có việc gì thì con thay đồ đi học nhé. Con đang hơi vội."'

    sup '"Ừ... lo ăn sáng rồi đi học đi con."'

    m '"Dạ vâng. Bye mẹ."'

    sup '"Bye con."'

    play sound "endp.mp3" volume 1.0

    pause 2.0

    nvl clear

    hide phone with fade

    pause 1.0
    
    m 'Haizz'

    "'Giờ con có hơi vội', 'Giờ con đang bận', 'Con đang ở trường',... là những câu tôi sử dụng mỗi lần tôi muốn kết thúc cuộc trò chuyện."

    'Điều này giúp tôi tránh những cuộc hội thoại mà tôi không muốn có với mẹ.'

    'Nhưng tôi biết, sẽ đến lúc tôi cần phải nói thật cho mẹ mọi thứ.'

    'Đúng vậy, sẽ đến lúc...'

    'Chỉ là lúc đấy không phải bây giờ.'

    nvl clear
    
#     "Sau khi đánh răng, rửa mặt, thay đồ; tôi dắt xe ra khỏi chỗ gửi xe của nhà trọ."


#     scene street
#     with fade
    
#     """
#     Tôi tính làm gì đó ăn sáng, nhưng có vẻ trong tủ lạnh không còn gì cả.

#     Có thịt heo để ở ngăn lạnh, giờ mà chờ băng tan ra thì lâu quá, còn lại thì là tí rau, sữa đặc, và sữa ở ngăn mát, 
#     giờ mà mua bánh mì thì lại hơi xa.

#     Mẹ tôi cứ như thần ấy, gửi đồ ăn cho tôi đúng lúc tôi sắp hết luôn. 
#     Đồ ăn ở thành phố lớn đúng đắt đỏ mà, nhưng thôi, giờ cứ lo lấp đầy bụng đã.
    
#     Tôi không phải là thiếu cẩn thận tới mức không để ý tình trạng tủ lạnh đâu. 
#     Chỉ là dạo này tôi lo học với đi làm thêm quá nên tôi không để ý đồ ăn.
    
#     {clear}

#     Chương trình học năm nhất thì nói khó cũng không đúng mà nói nó dễ thì cũng không phải. 
#     Có lẽ với riêng tôi thì thấy nó khá mệt và nặng.
    
#     Mấy môn đại cương còn bao gồm phải học môn chính trị với lý tưởng này nọ. 
#     Tôi thật sự không thấy ứng dụng thực tiễn của nó vào cuộc sống hằng ngày.
    
#     Rồi còn môn toán với các bài toán kinh tế. Tôi hiểu lí do phải học cái này nhưng lớp học đúng chán luôn. 
#     Thầy giảng mà tôi thấy chả chữ nào vào trong đầu cả.
    
#     Nói thật thì tôi cũng có mơ hồ tưởng tượng được việc này trước khi dô đại học rồi. 
#     Dô đây thì có phần thoải mái hơn khi học trung học phổ thông, với chương trình thoáng hơn, 
#     nhưng chắc chắn là khó hơn cũng rất nhiều. Đã dô đây học thì xác định tự bơi.
    
#     {clear}

#     Tôi cũng không tính đi học ban đầu đâu. Quê tôi là thành phố biển Sa Nam. 
#     Nói về du lịch thì nó cũng khá phát triển. Nếu tôi ở nhà với mẹ, đi làm phụ bếp ở 
#     mấy cái nhà hàng ngoài biển hay quán cà phê, rồi từ từ đi lên chức quản lí cũng được mà.
#     Còn nếu họ yêu cầu bằng cấp thì tôi ít nhất cũng tích vừa đủ tiền để ra làm kinh doanh riêng.
    
#     Mẹ tôi đương nhiên phản đối. Nói rằng tôi nên đi học đại học để sau này đỡ phải làm công nhân khổ cực như mẹ.
#     Nói xong thì mẹ còn bảo là mẹ đã tiết kiệm đủ tiền để con đi học rồi nên con cứ chọn trường đi.
    
#     Tôi cũng trăn trở lúc đó lắm. Mãi tôi mới tìm được một trường có điều kiện nhập học là 26 điểm 
#     trong kì thi tốt nghiệp và có ngành tôi muốn làm là quản trị kinh doanh.
#     Nhưng tôi thấy nó là trường tư thì vẫn phải hỏi lại mẹ xem mẹ chắc chắn cho tôi đi học ở đây không. 
    
#     Mẹ tôi cũng không bị bất ngờ gì, cũng nói là ổn. Chỉ bảo tôi chịu khó học là được.
    
#     {clear}

#     Tôi không phải người tài giỏi, hay quá đặc biệt tốt ở bất kì lĩnh vực nào.
#     Điều duy nhất tôi có hơn người khác là sự tự tin thôi. Nên khi mẹ ủng hộ tôi vậy, 
#     tôi cũng rất vui vẻ mà làm hồ sơ xin học.
    
#     Trường đại học Hương Sen nằm ở thành phố Ngọc Ánh, thủ đô kinh tế nước Đại Nam.
#     Nói về việc học kinh tế, lập nghiệp hay tìm kiếm cơ hôi việc làm 
#     trong các ngành nghề lớn nhỏ thì tới đây là một lựa chọn khôn ngoan.
    
#     Dù đi học ở đây nghĩa là tôi sẽ không về nhà với mẹ một thời gian dài. 
    
#     Hai mẹ con dù nói chuyện có vẻ hơi căng thẳng nhiều lúc nhưng cả tôi và mẹ đều khóc một chút trước khi chia xa.
    
#     {clear}

#     Tôi cũng đã sống ở Ngọc Ánh được một thời gian rồi. Tầm một tháng nếu tôi không nhớ nhầm.
    
#     Nơi này tôi thấy cái gì cũng có và nhộn nhịp hơn hẳn ở Sa Nam. Vấn đề duy nhất là giao thông thôi.
    
#     Ôi giao thông gì mà đông kinh khủng. Tôi lái xe đi học nãy giờ mà chỉ nhích lên được có ti tí. 
#     Không khéo lại muộn học mất.
    
#     Nếu như chỉ cần tôi dậy sớm đi học thì đỡ phải lo giao thông thì tôi cũng đã làm.
#     Nhưng bất luận là tôi có chọn đi sớm hay đi trễ, sáng hay tối, mưa hay nắng thì đường cứ đông.
#     Làm sao mà nó có thể chứa người 24/7 vi diệu vậy cơ chứ? 
    
#     Tôi nhiều lần tự hỏi, nhưng rất tiếc tôi không phải mấy người học đô thị. 
#     Chuyên ngành tôi là quản trị khách sạn - nhà hàng. Ít nhất, tôi có thể an ủi bản thân 
#     là dù tôi có rớt đại học mà phải ra làm ngoài thì tôi chắc sẽ dễ tìm khách ở đây hơn là ở Sa Nam.
    
#     {clear}

#     """

#     "Suy nghĩ viển vông mãi thì cũng tới cổng trường."
    
#     m '"Haizzz...."'
    
#     "Lái xe một cách điêu luyện vào cổng trường và hướng tới bãi gửi xe, tôi xuống xe 
#     và thở phào nhẹ nhõm khi thoát khỏi cái \"bãi người\" đó."
    
#     "Đến lúc vào lớp học rồi."
    
#     m '"..."'
    
#     "Mong là hôm nay ông thầy giao ít bài tập về nhà thôi."
    
#     "Tôi vẫn còn thấy oải khi nhớ về bài tập tối qua. Ugh. Làm ơn đừng có thêm mà"

#     nvl clear

#     scene courtyard with moveinright

#     "Áo khoác tôi mặc ngoài để che nắng bắt đầu bốc mùi mồ hôi. 
#     Nhưng tôi chưa thể vào lớp được, tôi còn cần ghé qua căn tin mua đồ ăn sáng đã."

#     "Đi vội tới căn tin trong khi vác theo máy tính trong cặp, tôi chảy mồ hôi dù đang đi dưới bóng mát." 
#     "Tôi thắc mắc tại sao tôi không dành thời gian thêm để tập thể dục." 
#     "Tôi không phải con trai, 
#     nhưng chả có gì là sai khi luyện tập tăng cơ bắp cả. Nếu tôi nhớ không nhầm thì trường có câu lạc bộ Taekwondo, 
#     tham gia để rèn luyện cơ thể hay kiếm điểm rèn luyện cũng được." 

#     nvl clear

#     scene canteen with moveinright
    
#     "Tôi cuối cùng cũng đã tới căn tin trường."
    
#     "Căn tin trường nằm ở phía bên trái tính từ cổng chính đi vào và ngược hướng hoàn toàn với bãi gửi xe, nên việc đi bộ qua đây khá mất công."
    
#     "Tôi thấy một hàng người chờ thu ngân ngay khi đi vào căn tin. Vậy là tôi vẫn phải chờ một lúc."
    
#     "Tôi xem xét việc nên mua gì. "
    
#     "Chắc giờ tôi mua cái bánh mì hay cái bánh bao rồi đi lên lớp luôn quá. 
#     Tôi cũng chả ngại việc tới muộn nhưng giờ tôi đang rất nóng mà căn tin họ chỉ gắn quạt chứ chả lắp máy lạnh, 
#     chỉ có lớp học là lắp máy lạnh thôi. Tôi không muốn ở lại đây lâu."
    
#     nvl clear

#     uk '"Uhm Chi này, bà có muốn đi lên trước không?"'
    
#     "Trong khi tôi đang bận suy nghĩ thì người đứng trước tôi trong hàng đợi bắt chuyện."
    
#     show truc

#     "Đó là một thanh niên nam, không quá cao hay quá thấp, tóc ngắn và đeo kính. 
#     Tôi nhìn vào mặt anh chàng này, cố nhớ xem mình đã từng gặp anh ta ở đâu chưa. 
#     Mặt thon và da hơi đen, mặc áo trắng. Hình như đúng là tôi đã thấy anh ta ở đâu rồi."
    
#     nvl clear

#     m '"Ờ... Ông hình như học chung lớp với tôi đúng không?"'
    
#     hide truc
#     show truc happy

#     uk '"Đúng rồi á!"'
    
#     "Anh chàng trả lời giọng hưng phấn. Việc tôi nhận ra anh có vẻ làm anh vui sướng lắm. 
#     Tôi thì chỉ nhớ mang máng mình từng thấy một người như anh ngồi chung trong lớp học. 
#     Ngồi cách nhau tận hai dãy bàn mà cả hai cũng chưa từng bắt chuyện với nhau bao giờ."
    
#     nvl clear

#     m '"Um, ông muốn nhường tôi lên trước hả? Thôi không cần đâu, ông cứ đứng trước đi, tôi chờ được mà."'
    
#     nvl clear

#     "Tôi thật sự không muốn đứng chờ ở đây đâu, nhưng ai mà biết ý định của tên này là gì. Cứ cẩn thận vẫn hơn."
    
#     hide truc happy
#     show truc

#     uk '"Không sao đâu mà. Tui cũng không vội gì mà tui thấy bà có vẻ mệt với mồ hôi lắm á. 
#     Bà đang vội thì đứng trước đi, tui chờ thêm tí cũng được."'
    
#     "Cái tên này có ý gì vậy nhỉ? "
    
#     "Tôi đã có ý từ chối anh ta vậy mà anh ta vẫn cố đẩy tôi lên. "
    
#     "Có thể tôi chỉ đang lo lắng thái quá, và thanh niên trước mặt tôi chỉ là có ý tốt mà thôi. "

#     nvl clear

#     menu:
#         "Chấp nhận lời đề nghị của anh thanh niên":
#             jump accept
    
# label accept:
#     "Suy nghĩ một lúc ngắn, tôi chấp nhận lời đề nghị của tên thanh niên."
    
#     nvl clear

#     m '"Uhm.... Cảm ơn ông."'
    
#     "Tôi cảm ơn tên thanh niên và đổi chỗ."
    
#     "Tên thanh niên vui vẻ cho tôi lên trước. Tôi đoán vẫn còn những người tốt bụng như tên này nhỉ."
    
#     "Tôi suy nghĩ chủ đề bắt chuyện, cũng chả có lí do gì sâu xa đâu, tôi chỉ nghĩ mình nên làm vậy mà thôi."
    
#     nvl clear

#     m '"Mà hình như tên ông là cái gì Trung đúng không?"'
    
#     uk '"Đâu, tên tôi là Trực mà. Trung gì ở đây?"'
    
#     m '"A, xin lỗi nha. Tại tui cũng hay quên á."'
    
#     t '"Hahah. Không sao đâu."'
    
#     "Tôi không thật sự cảm thấy ngại gì khi không nhớ tên của anh chàng này. 
#     Đã bao giờ nói chuyện với nhau đâu mà đòi nhớ."
    
#     "Nói chuyện chưa được bao lâu thì tôi cũng đến quầy thu ngân."
    
#     nvl clear

#     m '"Cô ơi, cho con cái bánh bao."'
    
#     sup '"15 ngàn con."'
    
#     "Cô thu ngân lớn tuổi chỉ trả lời ngắn gọn với yêu cầu của tôi. 
#     Cũng hợp lí, hàng vẫn còn người mà."
    
#     "Tôi đưa tiền và nhận bánh bao."
    
#     nvl clear

#     m '"Tui lên lớp trước nha."'

#     "Tôi quay lại nói về hướng tên thanh niên."
    
#     nvl clear

#     t '"Ừ bà lên trước đi."'
    
#     hide truc

#     "Tên này nãy giỡ cứ hí hửng mãi. Tôi chả có cảm nghĩ gì sâu xa về anh ta. 
#     Nhưng cuộc nói chuyện cũng không hẳn là buồn chán, không hiểu sao tôi cũng thấy tinh thần mình phấn chấn hơn hẳn. "
    
#     "Tôi không tin lắm vào tình yêu, dù bản thân tôi rất mê phim Hàn." 
#     "Nó hài hước, nó có phần thực tế, nó thú vị và diễn viên nào cũng đẹp cả." 
#     "Không có gì để chê những bộ phim như vậy. Vấn đề duy nhất là tôi không còn tin vào nó như trước đây nữa. "
    
#     nvl clear

#     "Phim ảnh, truyện tranh hay bất kì phương tiện truyền thông nào 
#     cũng không thật bằng cuộc sống hằng ngày và cuộc sống hằng ngày thì đầy thứ khổ sở và buồn chán." 
#     "Tôi phải luôn cố gắng và phải luôn tự lập. Tôi không được dựa dẫm quá nhiều vào ai." 
#     "Tình yêu và tình bạn chân thành chỉ xuất hiện trên phim ảnh mà thôi. "
#     "Người tới với nhau vì lợi ích và tôi cần phải là người hữu dụng. Đó là thực tế mà tôi chấp nhận."
    
#     nvl clear

#     "Người khác mà biết tôi nghĩ gì chắc sẽ nói tôi đang hơi tiêu cực quá." 
#     "Với tôi thì đây là cách lấy lại bình tĩnh cực kỳ hiệu quả." 
#     "Muốn kiểm soát cuộc đời bản thân thì trước tiên phải biết cách kiểm soát cảm xúc." 
#     "Chỉ với cái đầu lạnh thì tôi mới đưa ra lựa chọn sáng suốt mà thôi, và chỉ khi đưa ra được lựa chọn đúng 
#     tôi mới không phạm phải sai sót." 
#     "Đấy, suy nghĩ vậy cũng có cái tích cực mà, đâu phải tiêu cực hoàn toàn đâu."

#     nvl clear

#     scene classroom with fade
    
#     "Tôi bước vào lớp và nhìn xung quanh."
    
#     "Gần cuối lớp có lẻ tẻ vài người đang nói chuyện với nhau, tay cầm điện thoại hoặc mở máy tính. "
    
#     "Trong khi tôi còn đang loay hoay định hình xem chỗ nào còn ổ cắm để ngồi thì ai đó giơ tay lên gọi tôi."

#     nvl clear

#     uk '"Chi! Ngồi đây nè mày!"'
    
#     "Tôi nhìn về hướng người vừa gọi tên tôi."
    
#     show hong
    
#     "Một cô gái trẻ, mặc quần tây và áo phông với ống tay ngắn, cả bộ đều một màu trắng. 
#     Mái tóc hung của cô ấy xõa ra như tia nắng mặt trời. 
#     Nhưng ấn tượng nhất vẫn là đôi mắt to tròn và gương mặt tươi tắn đang gọi tên tôi như bạn lâu năm. 
#     Dù tôi biết rõ chúng tôi chưa quen nhau lâu đến vậy." 
    
#     "Cô ấy tên là Hồng, bạn học chung ngành quản trị kinh doanh với tôi. 
#     Tôi quen Hồng từ khi bắt đầu học đại học. Tôi cũng không quá thân thiết với Hồng 
#     nhưng so với những người khác trên lớp thì Hồng là người tôi nói chuyện nhiều nhất."
    
#     "Tôi vẫy tay qua loa trả lời Hồng rồi tiến về phía cô mà ngồi xuống."
    
#     nvl clear

#     h '"Chi ơiii. Mày chỉ tao câu này với. Tao làm từ tối qua mãi không được."'
    
#     "Hồng đẩy cuốn vở qua phía tôi, mắt long lanh, giả bộ mít ướt nhờ tôi giúp đỡ. "
    
#     "Tôi đón lấy cuốn vở từ tay Hồng và nhìn trang giấy từ trên xuống."
    
#     nvl clear

#     m '"Mày muốn tao chỉ câu nào?"'
    
#     h '"Câu 6 á mày. Tìm x phần trăm số người mua cần thiết. Tao tra online rồi thử hỏi OpenBot mà vẫn không ra kết quả."'
    
#     m '"Câu 6 của bài 5 đúng không? Câu này mày phải tính thêm giá sản xuất của sản phẩm nữa. Cũng dễ lắm, hiểu tí là làm ra à."'
    
#     "Bài tập này tối qua tôi đã hoàn thành xong rồi, nó dễ nhưng tốn thời gian để hiểu đúng vấn đề thôi."
    
#     "Nhìn bề ngoài, ai cũng nghĩ Hồng là người thân thiện, thông minh và dễ gần 
#     nhưng tôi biết thực tế của cô ấy là người ra sao. 
#     Nếu phải nói thì sự chủ động giao tiếp là điểm mạnh của Hồng, 
#     còn lại thì Hồng không được giỏi lắm dù ở môn học nào. 
#     Tôi thường phải chỉ lại cho Hồng từ đầu đến cuối, nhiều đến mức tôi còn ngạc nhiên. 
#     Hồng vẫn chịu khó lắng nghe và cố gắng tự học nên dù nhiều lúc khó chịu lắm, tôi vẫn bình tĩnh chỉ cho cô."
    
#     nvl clear

#     m '"Đấy ra rồi đó. {i}(Tôi nói với một giọng tự tin){/i}"'
    
#     h '"Uiiii, siêu quá. Cảm ơn mày nhaaa."'
    
#     "Hồng thường hay nhấn nhá ở những chữ như nha, ỏ, ơi,... khi nói chuyện, 
#     giống như đang cố tỏ ra dễ thương vậy. Tôi thì không ưa cái kiểu đó 
#     nhưng cũng không đến mức gọi là ghét, thấy nó cứ kì kì thế nào ấy."
    
#     "Trong lúc tôi tập trung chỉ bài cho Hồng, căn phòng học yên tĩnh đã ồn ào từ lúc nào. "
    
#     nvl clear

#     hide hong 

#     "Tôi lấy máy tính ra khỏi cặp để coi lại bài giảng, 
#     đọc một số tin tức và xem các trang khách sạn hay nhà hàng đang tuyển dụng 
#     để xem bản thân có thể ứng tuyển ở đâu. "
    
#     "Làm hồ sơ xin việc thì khá đơn giản nhưng tôi muốn có portfolio tốt hơn. 
#     Mà muốn có portfolio đẹp thì cần phải có kinh nghiệm làm việc 
#     ở những nơi có tiếng hoặc phải có thành tích học tập tốt. 
#     Xét về quan hệ để xin một slot ứng tuyển 
#     thì tôi chả quen ai ở thành phố Ngọc Ánh này cả, 
#     còn về thành tích học tập thì tôi tự thấy mình chỉ là trên trung bình mà thôi, 
#     không phải thiên tài hay học chuyên gì. "
    
#     "Tôi chỉ biết thở dài thất vọng vì bản thân thật yếu đuối, 
#     nhưng tôi đoán chuyện này cũng không phải của riêng ai. 
#     Nếu như ai cũng thành công với thiên tài thì Đại Nam đã nổi tiếng khắp 5 châu rồi. 
#     Thiên tài thì có cách của thiên tài, người bình thường thì có cách của người bình thường. 
#     Tôi cứ tiếp tục cố gắng tìm cách của tôi là được. "
    
#     "Tôi tiếp tục lăn con chuột và thưởng thức cái bánh bao mới mua, 
#     không bận tâm với bất kì điều gì khác."
    
#     nvl clear

    

#     play sound "<from 2 to 5>bell.mp3"

#     window hide
#     pause 3.0

#     "Tiếng chuông báo hiệu vào lớp vang lên. "
    
#     "Tôi rời mắt khỏi màn hình máy tính mà nhìn về phía bục giảng và cửa ra vào. 
#     Không vì lí do gì cả, chỉ là nhìn theo bản năng mà thôi."
    
#     "Nhưng đó là lúc tôi phát hiện cái tên Trực đi vào lớp cùng với một nhóm các nam thanh niên khác."
    
#     "Cả hai bọn tôi đều nhìn thấy nhau, nhưng không ai nói gì cả. 
#     Chỉ khẽ vẫy tay rồi tiếp tục công việc cá nhân thôi. "
    
#     "Tôi đoán anh ta cũng biết đọc tình hình đấy chứ."

#     nvl clear

#     show hong 

#     h '"Mày chào ai dị?"'
    
#     "Hồng phát hiện hành động chào của tôi với Trực và bắt đầu nghi vấn."
    
#     m '"Ai đâu?"'
    
#     "Tôi cố tình giả ngơ, nhằm dừng cuộc nói chuyện ở đây. "
    
#     h '"Hmmm"'
    
#     "Hồng chỉ nhìn tôi mà không nói gì. "

#     hide hong 
    
#     "Tôi cũng không nói gì thêm, chỉ tiếp tục di chuột, lướt màn hình máy tính."
    
#     "Đúng lúc này, thầy vào lớp."

#     nvl clear 

#     "{i}Trong buổi học{/i}"
    
    
#     "Lớp học diễn ra bình thường mà không có bất kì sự kiện gì đặc biệt"
    
#     nvl clear

#     "{i}Sau buổi học{/i}"
    
#     sup '"Vậy bài hôm nay kết thúc ở đây. Tuần sau mình sẽ thực hiện thuyết trình, 
#     coi như bài thi cuối kỳ và hoàn tất môn luôn. 
#     Vì bản chất là bài thi nên nó sẽ chiếm 80\% điểm trung bình, nếu điểm thấp thì cứ xác định học lại môn đi nhé. 
#     Giờ các em tự chọn nhóm rồi chủ đề đi. Làm xong thì đưa danh sách cho bạn lớp trưởng nhé. Giờ thầy đi có việc."'
    
#     "Thầy nhanh chóng thông báo về việc thi cử tuần sau và rời đi."
    
#     "Cả lớp xôn xao trước thông báo của thầy. "
    
#     "Đáng lẽ việc thông báo về hình thức thi hay cách chấm điểm nên được nói từ đầu học kỳ mới đúng. 
#     Điều này đúng là có nói, nhưng sau khi xét trình độ của lớp thì việc thi trắc nghiệm giấy không được khả quan. 
#     Thầy có vẻ đã chủ động đổi hình thức thi lại ở tuần học cuối cùng. 
#     Theo góc nhìn của tôi, quyết định của thầy cũng khá hợp lí, dù điều này có gây ngạc nhiên với nhiều thành viên trong lớp."
    
#     "Nhưng bỏ qua chuyện đó, việc của tôi giờ là phải tìm nhóm làm chung."
    
#     "Tôi và Hồng có thể làm thành một nhóm. Nhưng tôi không tin vào khả năng của Hồng lắm, 
#     nếu được thì chọn nhóm có người giỏi sẽ đỡ hơn."
    
#     nvl clear

#     show hong 

#     h '"Chi, vậy mình làm một nhóm đi ha?"'
    
#     "Hồng nhìn tôi với sự mong đợi."
    
#     "Làm gì bây giờ, tôi có nên tìm nhóm khác tốt hơn không hay làm cùng một nhóm với Hồng. "
    
#     "Đây là bài thi cuối kỳ, không thể làm chơi chơi được. Nhưng từ chối thì lại mất tình cảm."
    
#     "Trong lúc đang xem xét nên nói có hay không, từ đằng sau tôi, một bóng người tiến tới. "

#     show hong at left
    
#     show truc at right 
    
    
#     t '"Uhm Chi ơi, giờ nhóm tôi đang thiếu một thành viên á... Không biết bà đã chọn nhóm chưa?"'
    
#     "Trực đứng đối diện tôi và Hồng, yêu cầu tôi vào nhóm của cậu ta."
    
#     "Tôi nhìn về phía nhóm của Trực, đang ngồi lướt điện thoại là lớp trưởng, 
#     người mà tôi biết là có thể đảm nhận đồ án này."
    
#     nvl clear

#     h '"Ê, ông là ai dị? Tự nhiên chui ra lấy Chi khỏi nhóm tôi là sao?"'
    
#     "Hồng nhìn về phía Trực mà lên giọng, cố ý đuổi anh ta đi."
    
#     t '"Ể... Bà có nhóm rồi à Chi?"'
    
#     "Trực thật thà nhìn tôi mà hỏi."
    
#     m '"Uhm... Tui chưa"'
    
#     t '"Ồ vậy bà có muốn vào nhóm tui không?"'
    
#     "Tôi có hơi tò mò về ý định của Trực khi mời tôi vào nhóm, 
#     nhưng tôi đoán anh ta không có ý định gì xấu. 
#     Chắc do ấn tượng ban nãy ở căn tin vẫn còn hằn trong tâm trí tôi."
    
#     "Vậy bây giờ tôi nên chọn ai đây?"
    
#     "Một người tôi đã thân khá lâu nhưng khả năng hoàn thành đồ án là rất thấp. 
#     Hay một người tôi mới quen nhưng với khả năng làm đồ án cực kỳ khả quan."

#     nvl clear

#     menu:
#         "Chọn cùng nhóm với Trực":
#             jump choose_Truc
#         "Chọn cùng nhóm với Hồng":
#             jump choose_Hong
# label choose_Truc:
                
#     "Sau khi suy nghĩ một lúc thì tôi đưa ra quyết định của mình."

#     nvl clear

#     m '"Hmm, tui vào nhóm ông cũng được, nhưng...."'

#     h '"Ủa mày?"'

#     "Hồng nhìn tôi với đôi mắt tò mò khó hiểu."

#     nvl clear

#     h '"Mày không muốn vào nhóm tao à?"'

#     m '"Không phải là tao không muốn mà là tao muốn thử làm việc chung với nhiều người. 
#     Mày quen biết rộng thì vào làm nhóm khác cũng được mà."'

#     "Tôi dùng lí lẽ nhất thời tôi nghĩ được mà biện hộ cho việc lựa chọn Trực thay vì Hồng, 
#     cố gắng không làm mất lòng cô."

#     nvl clear

#     h '"Hmph."'

#     "Hồng nhìn tôi với vẻ mặt khó chịu, như một đứa trẻ ăn vạ 
#     vì ba mẹ không chịu mua đồ chơi cho nó vậy."

#     return

# label choose_Hong:


    


    # This ends the game.

    return
