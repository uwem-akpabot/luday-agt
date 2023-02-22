for service in bdn-blogs-api bdn-contact-api bdn-products-api bdn-user-api;
do 
    docker exec -i $service flask db init
    docker exec -i $service flask db migrate
    docker exec -i $service flask db upgrade
    
    if [ $service == "bdn-user-api" ]; then
        docker exec -i $service flask seed run
    fi
done   

for service in bdn-blogs-api  bdn-products-api bdn-user-api;
do
    if [ $service == "bdn-blogs-api" ]; then
            docker exec -i $service sh -c "cd ../../ && mkdir images && cd images && mkdir blogs"
    elif [ $service == "bdn-products-api" ]; then
            docker exec -i $service sh -c "cd ../../ && mkdir images && cd images && mkdir products vendors categories"
    elif [ $service == "bdn-user-api" ]; then
            docker exec -i $service sh -c "cd ../../ && mkdir images && cd images && mkdir vendors"
    fi
done