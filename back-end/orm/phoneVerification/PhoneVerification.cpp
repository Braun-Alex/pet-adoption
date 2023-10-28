//
// PhoneVerification.cpp
//
// This file has been generated from pet_adoption.xml. Do not edit.
//


#include "DatabaseSystem/PhoneVerification.h"


using namespace std::string_literals;
using namespace Poco::Data::Keywords;


namespace DatabaseSystem {


PhoneVerification::PhoneVerification(ID id):
	Poco::ActiveRecord::ActiveRecord<std::string>(id)
{
}


PhoneVerification::PhoneVerification(const PhoneVerification& other):
	Poco::ActiveRecord::ActiveRecord<std::string>(other),
	_phoneProof(other._phoneProof),
	_expirationAt(other._expirationAt),
	_used(other._used)
{
}


PhoneVerification::Ptr PhoneVerification::find(Poco::ActiveRecord::Context::Ptr pContext, const ID& id)
{
	Poco::ActiveRecord::StatementPlaceholderProvider::Ptr pSPP(pContext->statementPlaceholderProvider());
	PhoneVerification::Ptr pObject(new PhoneVerification);

	pContext->session()
		<< "SELECT proofOfAuthority, phoneProof, expirationAt, used"
		<< "  FROM phone_verification"
		<< "  WHERE proofOfAuthority = " << pSPP->next(),
		into(pObject->mutableID()),
		into(*pObject),
		bind(id),
		now;

	return withContext(pObject, pContext);
}


void PhoneVerification::insert()
{
	Poco::ActiveRecord::StatementPlaceholderProvider::Ptr pSPP(context()->statementPlaceholderProvider());

	context()->session()
		<< "INSERT INTO phone_verification (proofOfAuthority, phoneProof, expirationAt, used)"
		<< "  VALUES (" << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ")",
		bind(id()),
		use(*this),
		now;
}


void PhoneVerification::update()
{
	Poco::ActiveRecord::StatementPlaceholderProvider::Ptr pSPP(context()->statementPlaceholderProvider());

	context()->session()
		<< "UPDATE phone_verification"
		<< "  SET phoneProof = " << pSPP->next() << ", expirationAt = " << pSPP->next() << ", used = " << pSPP->next()
		<< "  WHERE proofOfAuthority = " << pSPP->next(),
		use(*this),
		bind(id()),
		now;
}


void PhoneVerification::remove()
{
	Poco::ActiveRecord::StatementPlaceholderProvider::Ptr pSPP(context()->statementPlaceholderProvider());

	context()->session()
		<< "DELETE FROM phone_verification"
		<< "  WHERE proofOfAuthority = " << pSPP->next(),
		bind(id()),
		now;
}


const std::vector<std::string>& PhoneVerification::columns()
{
	static const std::vector<std::string> cols =
	{
		"proofOfAuthority"s,
		"phoneProof"s,
		"expirationAt"s,
		"used"s,
	};

	return cols;
}


const std::string& PhoneVerification::table()
{
	static const std::string t = "phone_verification";
	return t;
}


} // namespace DatabaseSystem
