//
// EmailVerification.cpp
//
// This file has been generated from pet_adoption.xml. Do not edit.
//


#include "DatabaseSystem/EmailVerification.h"


using namespace std::string_literals;
using namespace Poco::Data::Keywords;


namespace DatabaseSystem {


EmailVerification::EmailVerification(ID id):
	Poco::ActiveRecord::ActiveRecord<std::string>(id)
{
}


EmailVerification::EmailVerification(const EmailVerification& other):
	Poco::ActiveRecord::ActiveRecord<std::string>(other),
	_emailProof(other._emailProof),
	_expirationAt(other._expirationAt),
	_used(other._used)
{
}


EmailVerification::Ptr EmailVerification::find(Poco::ActiveRecord::Context::Ptr pContext, const ID& id)
{
	Poco::ActiveRecord::StatementPlaceholderProvider::Ptr pSPP(pContext->statementPlaceholderProvider());
	EmailVerification::Ptr pObject(new EmailVerification);

	pContext->session()
		<< "SELECT proofOfAuthority, emailProof, expirationAt, used"
		<< "  FROM email_verification"
		<< "  WHERE proofOfAuthority = " << pSPP->next(),
		into(pObject->mutableID()),
		into(*pObject),
		bind(id),
		now;

	return withContext(pObject, pContext);
}


void EmailVerification::insert()
{
	Poco::ActiveRecord::StatementPlaceholderProvider::Ptr pSPP(context()->statementPlaceholderProvider());

	context()->session()
		<< "INSERT INTO email_verification (proofOfAuthority, emailProof, expirationAt, used)"
		<< "  VALUES (" << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ")",
		bind(id()),
		use(*this),
		now;
}


void EmailVerification::update()
{
	Poco::ActiveRecord::StatementPlaceholderProvider::Ptr pSPP(context()->statementPlaceholderProvider());

	context()->session()
		<< "UPDATE email_verification"
		<< "  SET emailProof = " << pSPP->next() << ", expirationAt = " << pSPP->next() << ", used = " << pSPP->next()
		<< "  WHERE proofOfAuthority = " << pSPP->next(),
		use(*this),
		bind(id()),
		now;
}


void EmailVerification::remove()
{
	Poco::ActiveRecord::StatementPlaceholderProvider::Ptr pSPP(context()->statementPlaceholderProvider());

	context()->session()
		<< "DELETE FROM email_verification"
		<< "  WHERE proofOfAuthority = " << pSPP->next(),
		bind(id()),
		now;
}


const std::vector<std::string>& EmailVerification::columns()
{
	static const std::vector<std::string> cols =
	{
		"proofOfAuthority"s,
		"emailProof"s,
		"expirationAt"s,
		"used"s,
	};

	return cols;
}


const std::string& EmailVerification::table()
{
	static const std::string t = "email_verification";
	return t;
}


} // namespace DatabaseSystem
