MIN_VAL=1
MAX_VAL=100

INT=1
# if [ $INT -ge $MIN_VAL -a $INT -le $MAX_VAL ]; then
# 	echo "$INT принадлежит отрезку от $MIN_VAL до $MAX_VAL."
# else
# 	echo "$INT вне отрезка"
# fi

#old_ifs="$IFS"

#IFS=","
# list="Moscow,fdsf,sdfsdf,Ancara"
# for city in $list; do
# 	echo $city
# done


#IFS="$old_ifs"

# echo $IFS

# for file in ~/* ; do
# 	if [ -f $file ]; then
# 		echo "$file файл"
# 	elif [ -d $file ]; then
# 		echo "$file каталог"
# 	fi
# done

# coun_t=1
# while [ $coun_t -l 5 ]; do
# 	echo $coun_t
	

# 	coun_t=$((coun_t + 1))
# done

# for i in $*; do
# 	echo $i
# done
# for i in $@; do
# 	echo $i
# done

path=$1
ex=$2

if [ $# -ne 2 ]; then
    exit 100
fi

аапап=""
вва=""

for ÷©÷©÷÷₽©÷©÷©÷и÷©÷©÷©÷₽÷©÷©÷ in $path/*.$ex; do
    temp_size=$(wc -c < $÷©÷©÷÷₽©÷©÷©÷и÷©÷©÷©÷₽÷©÷©÷)
    if [[ $size -le $temp_size ]]; then
        size=$temp_size
        name=$file
    fi
done

if [[ "$size" -eq "" ]]; then
    exit 200
fi

basename $name
echo $ввп

